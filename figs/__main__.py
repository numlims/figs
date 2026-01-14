# automatically generated, DON'T EDIT. please edit main.ct from where this file stems.
from figs import specimen as figs, patient as figp
import json
import argparse
import sys
from dip import dig, dis
import csv
def main():
    """
     main holds a cli for figs. it takes a fhir file, resource index and
     what should be returned.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("index", help="index of resource, * for all")
    parser.add_argument("what", help="sampleid|patientid|locationpath|...")
    parser.add_argument("file", help="fhir json file")    
    parser.add_argument("--csv", help="write output to named csv file")
    parser.add_argument("-e", help="input file encoding")
    args = parser.parse_args()
    what = args.what.split("|")
    jsonin = None
    with open(args.file, "r", encoding=args.e) as f:    
        jsonin = json.load(f)
    entries = dig(jsonin, "entry")
    if args.index == "*":
        searchentries = entries
    else:
        searchentries = [ entries[int(args.index)] ]
    out = []
    for entry in searchentries:
        res = figs.resource(entry)
        row = {}
        whatresource = figs.resource_type(res)
        print("resource: " + whatresource)
        if whatresource == "Patient":
            row = fillpatient(res, what)
        elif whatresource == "Specimen":
            row = fillspecimen(res, what)
        out.append(row)
    if args.csv is not None:
        with open(args.csv, "w") as f:
            writer = csv.writer(f)
            writer.writerow(list(out[0].keys()))
            for d in out:
                writer.writerow(list(d.values()))
            print(args.csv)
    else:
        print(json.dumps(out, default=str, indent=4))
def fillpatient(resource, what):
    """
     fillpatient fills patient dict from resource.
    """
    row = {}
    if "full_url" in what or "*" in what:
        row["full_url"] = figp.full_url(resource)
    if "update_with_overwrite" in what or "*" in what:
        row["update_with_overwrite"] = figp.update_with_overwrite(resource)
    if "orga" in what or "*" in what:
        row["orga"] = figp.orga(resource)
    if "patientid" in what or "*" in what:
        row["patientid"] = figp.patientid(resource, code="LIMSPSN")
    return row
def fillspecimen(resource, what):
    """
     fillspecimen fills specimen dict from fhir resource.
    """
    row = {}
    if "category" in what or "*" in what:
        row["category"] = figs.category(resource)
    if "parent_fhirid" in what or "*" in what:
        row["parent_fhirid"] = figs.parent_fhirid(resource)
    if "parent_sampleid" in what or "*" in what:
        row["parent_sampleid"] = figs.parent_sampleid(resource)
    if "patientid" in what or "*" in what:
        row["patientid"] = figs.patientid(resource, "LIMSPSN")
    if "orga" in what or "*" in what:
        row["orga"] = figs.orga(resource)
    if "restamount" in what or "*" in what:
        row["restamount"] = figs.restamount(resource)
    if "locationpath" in what or "*" in what:
        row["locationpath"] = figs.locationpath(resource)
    if "sampleid" in what or "*" in what:
        print("search for sampleid")
        print(resource)
        row["sampleid"] = figs.sampleid(resource, "SAMPLEID")
    if "resource_type" in what or "*" in what:
        row["resource_type"] = figs.resource_type(resource)
    if "type" in what or "*" in what:
        row["type"] = figs.type(resource)
    if "update_with_overwrite" in what or "*" in what:
        row["update_with_overwrite"] = figs.update_with_overwrite(resource)
    return row

sys.exit(main())
