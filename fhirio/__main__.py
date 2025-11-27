# automatically generated, DON'T EDIT. please edit main.ct from where this file stems.
    import fhirio as fio
    import json
    import argparse
def main():
    """
     main holds a cli for fhirio. it takes a fhir file, resource index and
     what should be returned.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="fhir json file")
    parser.add_argument("index", help="index of resource, * for all")
    parser.add_argument("what", help="sampleid|patientid|locationpath|...")
    parser.add_argument("--csv", help="write output to named csv file")
    args = parser.parse_args()
    what = args.what.split("|")
    jsonin = None
    with open(os.path.join(dir, file), "r", encoding=encoding) as f:    
        jsonin = json.load(f)
    entries = dig(jsonin, "entry")
    if args.index == "*":
        searchentries = entries
    else:
        searchentries = [ entries[int(args.index)] ]
    out = []
    for entry in searchentries:
        res = fio.resource(entry)
        row = {}
        if "category" in what:
            row["category"] = fio.category(res)
        if "parent_fhirid" in what:
            row["parent_fhirid"] = fio.parent_fhirid(res)
        if "parent_sampleid" in what:
            row["parent_sampleid"] = fio.parent_sampleid(res)
        if "patientid" in what:
            row["patientid"] = fio.patientid(res, "LIMSPSN")
        if "orga" in what:
            row["orga"] = fio.orga(res)
        if "restamount" in what:
            row["restamount"] = fio.restamount(res)
        if "locationpath" in what:
            row["locationpath"] = fio.locationpath(res)
        if "sampleid" in what:
            row["sampleid"] = fio.sampleid(res, "SAMPLEID")
        if "resource_type" in what:
            row["resource_type"] = fio.resource_type(res)
        if "type" in what:
            row["type"] = fio.type(res)
        if "update_with_overwrite" in what:
            row["update_with_overwrite"] = fio.update_with_overwrite(res)
    if args.csv is not None:
        with open(args.csv, "w") as f:
            writer = csv.writer(f)
            writer.writerow(list(out[0].keys()))
            for d in out:
                writer.writerow(list(d.values()))
    else:
        print(json.dumps(out, default=str))


sys.exit(main())
