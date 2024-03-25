from pathlib import Path

import pytest
from mktestdocs import check_md_file

PYTHON_CODE_DIRECTORY = Path(__file__).parent / "../docs/libraries/python-sdk"


@pytest.mark.parametrize(
    "fpath", PYTHON_CODE_DIRECTORY.glob("**/*.md"), ids=str
)
def test_run_python_code(fpath):
    check_md_file(fpath=fpath)
