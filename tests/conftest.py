# tests/conftest.py
import pytest
import pandas as pd
from pathlib import Path
from app.agent.tools.product_search import ProductSearchTool


@pytest.fixture
def mock_csv_file(tmp_path: Path):
    data = []
    df = pd.DataFrame(data)
    csv_path = tmp_path / "cars.csv"
    df.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture(scope="function")
def tool(mock_csv_file):
    return ProductSearchTool()