from blue_ai.help.generic import help_functions as generic_help_functions
from blue_ai.help.actions import help_perform_action
from blue_ai.help.assets import help_functions as help_assets
from blue_ai.help.aws_batch import help_functions as help_aws_batch
from blue_ai.help.blueness import help_blueness
from blue_ai.help.browse import help_browse
from blue_ai.help.conda import help_functions as help_conda
from blue_ai.help.clone import help_clone
from blue_ai.help.docker import help_functions as help_docker
from blue_ai.help.download import help_download
from blue_ai.help.env import help_functions as help_env
from blue_ai.help.eval import help_eval
from blue_ai.help.gif import help_gif
from blue_ai.help.git import help_functions as help_git
from blue_ai.help.gpu import help_functions as help_gpu
from blue_ai.help.host import help_functions as help_host
from blue_ai.help.init import help_init
from blue_ai.help.instance import help_functions as help_instance
from blue_ai.help.latex import help_functions as help_latex
from blue_ai.help.logging import help_cat
from blue_ai.help.logging import help_functions as help_log
from blue_ai.help.list import help_functions as help_list
from blue_ai.help.ls import help_ls
from blue_ai.help.metadata import help_functions as help_metadata
from blue_ai.help.mlflow import help_functions as help_mlflow
from blue_ai.help.notebooks import help_functions as help_notebooks
from blue_ai.help.object import help_functions as help_object
from blue_ai.help.open import help_open
from blue_ai.help.papertrail import help_functions as help_papertrail
from blue_ai.help.pause import help_pause
from blue_ai.help.plugins import help_functions as help_plugins
from blue_ai.help.publish import help_functions as help_publish
from blue_ai.help.repeat import help_repeat
from blue_ai.help.sagemaker import help_functions as help_sagemaker
from blue_ai.help.seed import help_functions as help_seed
from blue_ai.help.select import help_select
from blue_ai.help.session import help_functions as help_session
from blue_ai.help.storage import help_functions as help_storage
from blue_ai.help.sleep import help_sleep
from blue_ai.help.source import (
    help_source_caller_suffix_path,
    help_source_path,
)
from blue_ai.help.ssm import help_functions as help_ssm
from blue_ai.help.terminal import help_badge
from blue_ai.help.terraform import help_functions as help_terraform
from blue_ai.help.upload import help_upload
from blue_ai.help.watch import help_watch

help_functions = generic_help_functions(plugin_name="blue_ai")


help_functions.update(
    {
        "assets": help_assets,
        "aws_batch": help_aws_batch,
        "badge": help_badge,
        "blueness": help_blueness,
        "browse": help_browse,
        "cat": help_cat,
        "clone": help_clone,
        "conda": help_conda,
        "docker": help_docker,
        "download": help_download,
        "env": help_env,
        "eval": help_eval,
        "gif": help_gif,
        "git": help_git,
        "gpu": help_gpu,
        "host": help_host,
        "init": help_init,
        "instance": help_instance,
        "latex": help_latex,
        "log": help_log,
        "list": help_list,
        "ls": help_ls,
        "metadata": help_metadata,
        "mlflow": help_mlflow,
        "notebooks": help_notebooks,
        "object": help_object,
        "open": help_open,
        "pause": help_pause,
        "perform_action": help_perform_action,
        "plugins": help_plugins,
        "publish": help_publish,
        "repeat": help_repeat,
        "sagemaker": help_sagemaker,
        "seed": help_seed,
        "select": help_select,
        "sleep": help_sleep,
        "session": help_session,
        "storage": help_storage,
        "source_caller_suffix_path": help_source_caller_suffix_path,
        "source_path": help_source_path,
        "ssm": help_ssm,
        "terraform": help_terraform,
        "trail": help_papertrail,
        "upload": help_upload,
        "watch": help_watch,
    }
)
