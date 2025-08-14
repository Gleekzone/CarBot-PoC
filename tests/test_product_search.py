# tests/test_product_search.py
import pytest

@pytest.mark.skip(reason="pending refactoring test")
def test_product_search_tool(tool):
    """Test the product search tool with a mock CSV file."""
    results = tool.search("Volkswagen Touareg")
    assert any("Volkswagen Touareg" in res for res in results)
    

@pytest.mark.skip(reason="pending refactoring test")
def test_product_search_tool_no_results(tool):
    """Test the product search tool with a query that returns no results."""
    results = tool.search("Nonexistent Model")
    print(results)
    assert results[0] == "No cars found matching your search."
