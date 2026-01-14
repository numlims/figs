# automatically generated, DON'T EDIT. please edit test.ct from where this file stems.
from figs import specimen as figs
import json
def test_some():
    """
     test_some tries to get a sampleid from a fhir resource with figs.
    """
    with open("test/in/2025-09-26_16-12-56_Specimen_p0.json", encoding="latin-1") as f:
        jsonin = json.load(f)
        entry = jsonin["entry"][0]
        res = figs.resource(entry)
        sampleid = figs.sampleid(res)
        assert sampleid == "1477760201"
