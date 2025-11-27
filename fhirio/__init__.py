# automatically generated, DON'T EDIT. please edit init.ct from where this file stems.
from dip import dig, dis
class fhirhelp:
    @staticmethod
    def category(resource):
        """
         category returns the type from resource, 'MASTER', or 'ALIQUOTGROUP' or 'DERIVED' (this corresponds to dtype in the db). (was type).
        """
        ext = fhirhelp.extension(resource, "https://fhir.centraxx.de/extension/sampleCategory")
        return dig(ext, "valueCoding/code")
    @staticmethod
    def extension(resource, url:str):
        """
         extension gives the extension with the specified url.
        """
        exts = dig(resource, "extension")
        if exts is None:
            return None
        for ext in exts:
            if dig(ext, "url") == url:
                return ext
    @staticmethod
    def locationpath(resource):
        """
         locationpath gets the sampleLocation. (was lagerort).
        """
        exta = fhirhelp.extension(resource, "https://fhir.centraxx.de/extension/sample/sampleLocation")
        extb = fhirhelp.extension(exta, "https://fhir.centraxx.de/extension/sample/sampleLocationPath")
        return dig(extb, "valueString")
    @staticmethod
    def parent_fhirid(resource):
        """
         parent_fhirid gets the fhirid of the parent from resource.
        """
        if not "parent" in resource:
            return None
        return dig(resource, "parent/0/reference") # there should only be one parent, so one element in the array
    @staticmethod
    def parent_sampleid(resource):
        """
         parent_sampleid gets the sample id of the parent.
        """
        if "parent" in resource:
            for parent in dig(resource, "parent"):
                if not "identifier" in parent:
                    continue
                for coding in dig(parent, "identifier/type/coding"):
                    if dig(coding, "code") == "SAMPLEID":
                        return dig(parent, "identifier/value") # pid: parent id
        return None
    @staticmethod
    def patientid(resource, code:str="LIMSPSN"):
        """
         patientid gets the lims psn of the patient. (was limspsn).
        """
        for coding in dig(resource, "subject/identifier/type/coding"):
            if dig(coding, "code") == code:
                return dig(resource, "subject/identifier/value")
    @staticmethod
    def orga(resource):
        """
         orga returns the organisation or None if no organisation.
        """
        ext = fhirhelp.extension(resource, "https://fhir.centraxx.de/extension/sample/organizationUnit")
        return dig(ext, "valueReference/identifier/value")
    @staticmethod
    def restamount(resource):
        """
         restamount returns the restmenge of the sample. (was restmenge)
        """
        # pres = DictPath(resource)
        #if not "value" in resource["container"][0]["specimenQuantity"]:
        #    return None
        #return resource["container"][0]["specimenQuantity"]["value"]
        return dig(resource, "container/0/specimenQuantity/value")
    @staticmethod
    def sampleid(resource, code:str="SAMPLEID"):
        """
         sampleid returns the sample id of a resource.
        """
        return dig(fhirhelp.identifiers(resource), code)
    @staticmethod
    def type(resource):
        """
         type returns the material type of the resource. (was material).
        """
        return dig(resource, "type/coding/0/code")
    @staticmethod
    def update_with_overwrite(resource) -> bool:
        """
         update_with_overwrite returns update with overwrite of a resource.
        """
        ext = fhirhelp.extension(resource, "https://fhir.centraxx.de/extension/updateWithOverwrite")
        return dig(ext, "valueBoolean")
    @staticmethod
    def identifiers(resource):
        """
         identifiers returns the identifiers of a resource as dict keyed by the identifier codes, eg: { "SAMPLEID": "abc", "EXTSAMPLEID": "cde" }
        """
        out = {}
        if "identifier" not in resource:
            return None
        for identifier in dig(resource, "identifier"):
            codings = dig(identifier, "type/coding")
            if codings == None:
                continue
            for coding in codings:
                if dig(coding, "system") == "urn:centraxx":
                    # take the code as key. the value is a field of identifier.
                    key = dig(coding, "code")
                    out[key] = dig(identifier, "value")
        return out
    @staticmethod
    def resourceType(resource):
        """
         resourceType returns the resource type, Specimen or Observation.
        """
        return dig(resource, "resourceType")

