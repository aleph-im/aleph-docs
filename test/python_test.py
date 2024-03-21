import pathlib
import pytest
from mktestdocs import check_md_file


@pytest.mark.parametrize(
    "fpath", pathlib.Path("../docs/libraries/python-sdk").glob("**/*.md"), ids=str
)
def test_run_python_code(fpath):
    check_md_file(fpath=fpath)
