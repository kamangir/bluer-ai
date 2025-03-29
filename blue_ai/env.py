import os

from blue_options.env import load_config, load_env
from blue_objects.env import ABCLI_AWS_S3_BUCKET_NAME, ABCLI_AWS_S3_PREFIX

load_env(__name__)
load_config(__name__)


abcli_is_github_workflow = os.getenv("GITHUB_ACTIONS", "")

abcli_blue_sbc_application = os.getenv("abcli_blue_sbc_application", "")

abcli_display_fullscreen = os.getenv("abcli_display_fullscreen", "")

abcli_git_ssh_key_name = os.getenv("abcli_git_ssh_key_name", "")

abcli_gpu = os.getenv("abcli_gpu", "")

ABCLI_MESSENGER_RECIPIENTS = os.getenv("ABCLI_MESSENGER_RECIPIENTS", "")

abcli_path_abcli = os.getenv("abcli_path_abcli", "")

ABCLI_PATH_IGNORE = os.getenv("ABCLI_PATH_IGNORE", "")

abcli_papertrail_dest_host = os.getenv("abcli_papertrail_dest_host", "")
abcli_papertrail_dest_port = os.getenv("abcli_papertrail_dest_port", "")

VANWATCH_TEST_OBJECT = os.getenv("VANWATCH_TEST_OBJECT", "vanwatch-test-object-v2")

ABCLI_MLFLOW_STAGES = os.getenv("ABCLI_MLFLOW_STAGES", "")

ABCLI_AWS_BATCH_JOB_STATUS_LIST = os.getenv("ABCLI_AWS_BATCH_JOB_STATUS_LIST", "")
