# automatically generated, DON'T EDIT. please edit init.ct from where this file stems.
from dip import dig, dis

class figs:
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
    def full_url(entry):
        """
         full_url return the full url of a fhir entry.
        """
        return dig(entry, "fullUrl")
    @staticmethod
    def identifiers(resource):
        """
         identifiers returns the identifiers of a resource as dict keyed by the
         identifier codes, eg: { "SAMPLEID": "abc", "EXTSAMPLEID": "cde" }
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
    def resource(entry):
        """
         resource returns the resource for an entry.
         
         all other methods take resource as argument.
        """
        return dig(entry, "resource")
    @staticmethod
    def resource_type(resource):
        """
         resource_type returns the resource type, Specimen or Observation. (was resourceType).
        """
        return dig(resource, "resourceType")
    @staticmethod
    def update_with_overwrite(resource) -> bool:
        """
         update_with_overwrite returns update with overwrite of a resource.
        """
        ext = figs.extension(resource, "https://fhir.centraxx.de/extension/updateWithOverwrite")
        return dig(ext, "valueBoolean")
class specimen(figs):
    @staticmethod
    def category(resource):
        """
         category returns the type from resource, 'MASTER', or 'ALIQUOTGROUP'
         or 'DERIVED' (this corresponds to dtype in the db). (was type).
        """
        ext = figs.extension(resource, "https://fhir.centraxx.de/extension/sampleCategory")
        return dig(ext, "valueCoding/code")
    @staticmethod
    def centrifugation_date(resource):
        """
         centrifugation_date returns the centrifugation date.
        """
        sprecext = figs.extension(resource, "https://fhir.centraxx.de/extension/sprec")
        centriext = figs.extension(sprecext, "https://fhir.centraxx.de/extension/sprec/preCentrifugationDelayDate")
        return dig(centriext, "valueDateTime")
    @staticmethod
    def collected_date(resource):
        """
         collected_date returns the collection date.
        """
        return dig(resource, "collection/collectedDateTime")
    @staticmethod
    def container(resource):
        """
         container returns the container.
        """
        return dig(resource, "container/0/identifier/0/value")
    @staticmethod
    def derival_date(resource):
        """
         derival_date returns the derival date.
        """
        e = figs.extension(resource, "https://fhir.centraxx.de/extension/sample/derivalDate")
        return dig(e, "valueDateTime")
    @staticmethod
    def initialamount(resource):
        """
         initialamount returns the initial amount of the sample.
        """
        return dig(resource, "collection/quantity/value")
    @staticmethod
    def initialamountunit(resource):
        """
         initialamountunit returns the unit of the sample's initial amount.
        """
        return dig(resource, "collection/quantity/unit")
    @staticmethod
    def locationpath(resource):
        """
         locationpath gets the sampleLocation. (was lagerort).
        """
        exta = figs.extension(resource, "https://fhir.centraxx.de/extension/sample/sampleLocation")
        extb = figs.extension(exta, "https://fhir.centraxx.de/extension/sample/sampleLocationPath")
        return dig(extb, "valueString")
    @staticmethod
    def orga(resource):
        """
         orga returns the organisation or None if no organisation.
        """
        ext = figs.extension(resource, "https://fhir.centraxx.de/extension/sample/organizationUnit")
        return dig(ext, "valueReference/identifier/value")
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
         patientid gets the patient id of the subject.
        """
        for coding in dig(resource, "subject/identifier/type/coding"):
            if dig(coding, "code") == code:
                return dig(resource, "subject/identifier/value")
    @staticmethod
    def received_date(resource):
        """
         received_date returns the received date.
        """
        return dig(resource, "receivedTime")
    @staticmethod
    def reposition_date(resource):
        """
         reposition_date returns the reposition date.
        """
        e = figs.extension(resource, "https://fhir.centraxx.de/extension/sample/repositionDate")
        return dig(e, "valueDateTime")        
    @staticmethod
    def restamount(resource):
        """
         restamount returns the restmenge of the sample.
        """
        return dig(resource, "container/0/specimenQuantity/value")
    @staticmethod
    def restamountunit(resource):
        """
         restamountunit returns unit of the sample's restamount.
        """
        return dig(resource, "container/0/specimenQuantity/unit")
    @staticmethod
    def sampleid(resource, code:str="SAMPLEID"):
        """
         sampleid returns the sample id of a resource.
        """
        return dig(figs.identifiers(resource), code)
    @staticmethod
    def sprec(resource, name:str, key:str="valueCoding"):
        """
         sprec gets sprec of given name with key, default "valueCoding".
        """
        sprecext = figs.extension(resource, "https://fhir.centraxx.de/extension/sprec")
        ext = figs.extension(sprecext, "https://fhir.centraxx.de/extension/sprec/" + code)
        return dig(ext, key)
    #`stockprocessing``
    @staticmethod
    def type(resource):
        """
         type returns the material type of the resource. (was material).
        """
        return dig(resource, "type/coding/0/code")
class patient(figs):
    @staticmethod
    def patientid(resource, code:str="LIMSPSN"):
        """
         patientid returns the patientid by code.
        """
        return dig(figs.identifiers(resource), code)
    @staticmethod
    def orga(resource):
        """
         orga returns the organization unit for a patient resource.
        """
        return dig(resource, "generalPractitioner/0/identifier/value")
