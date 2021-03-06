import reconcile.queries as queries

from utils.gitlab_api import GitLabApi


QONTRACT_INTEGRATION = 'gitlab-ci-skipper'


def run(dry_run, gitlab_project_id=None, gitlab_merge_request_id=None):
    instance = queries.get_gitlab_instance()
    settings = queries.get_app_interface_settings()
    gl = GitLabApi(instance, project_id=gitlab_project_id,
                   settings=settings)
    labels = gl.get_merge_request_labels(gitlab_merge_request_id)
    output = 'yes' if 'skip-ci' in labels else 'no'
    print(output)
