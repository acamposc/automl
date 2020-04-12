def daily_automl(event, context):
    from google.cloud.devtools import cloudbuild_v1
    import os
    client = cloudbuild_v1.CloudBuildClient()

    project_id = os.getenv('GOOGLE_CLOUD_PROJ')
    trigger_id = os.getenv('CLOUD_BUILD_TRIGGER_ID')
    source = {'branch_name': os.getenv('BRANCH_NAME')}
    response = client.run_build_trigger(project_id, trigger_id, source)
