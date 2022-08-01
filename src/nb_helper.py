from typing import Union
from tqdm import tqdm as non_notebook_tqdm
from tqdm.notebook import tqdm as notebook_tqdm
try:
    from IPython.core.display import HTML
except:
    pass

Str_or_List = Union[str, list]


# ====================
def str_or_list_to_list(input_: Str_or_List) -> list:

    if isinstance(input_, str):
        return [input_]
    elif isinstance(input_, list):
        return input_


# ====================
def get_tqdm() -> type:
    """Return tqdm.notebook.tqdm if code is being run from a notebook,
    or tqdm.tqdm otherwise"""

    if is_running_from_ipython():
        tqdm_ = notebook_tqdm
    else:
        tqdm_ = non_notebook_tqdm
    return tqdm_


# ====================
def is_running_from_ipython():
    """Determine whether or not the current script is being run from
    a notebook"""

    try:
        # Notebooks have IPython module installed
        from IPython import get_ipython
        return True
    except ModuleNotFoundError:
        return False
