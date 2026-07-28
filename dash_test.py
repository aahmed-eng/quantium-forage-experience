from dash_app import header, visualization, region_picker


def test_header_is_present():
    assert header is not None
    assert header.id == "header"
    assert header.children == "Pink Morsel Visualizer"


def test_visualization_is_present():
    assert visualization is not None
    assert visualization.id == "visualization"
    assert visualization.figure is not None


def test_region_picker_is_present():
    assert region_picker is not None
    assert region_picker.id == "region_picker"
    assert region_picker.value == "north"
    assert "all" in region_picker.options
