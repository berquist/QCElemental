# Sources

* [srd144_Atomic_Weights_and_Isotopic_Compositions_for_All_Elements.json](srd144_Atomic_Weights_and_Isotopic_Compositions_for_All_Elements.json) from https://nist.gov/srd/srd_data//srd144_Atomic_Weights_and_Isotopic_Compositions_for_All_Elements.json downloaded 30 Aug 2018. A related website is https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses
* [element_names.py](element_names.py) from https://www.nist.gov/pml/periodic-table-elements `NIST SP 966 (July 2018)` downloaded 30 Aug 2018
* [longest_lived_isotope_for_unstable_elements.py](longest_lived_isotope_for_unstable_elements.py) from https://www.nist.gov/pml/periodic-table-elements `NIST SP 966 (July 2018)` downloaded 30 Aug 2018
* [srd121_nist-codata-fundamental-physical-constants-2014.json](srd121_nist-codata-fundamental-physical-constants-2014.json) (CODATA 2014) from https://nist.gov/srd/srd_data//srd121_allascii_2014.json downloaded 1 Sep 2018 off https://catalog.data.gov/dataset/nist-codata-fundamental-physical-constants-srd-121.
* [srd121_nist-codata-fundamental-physical-constants-2014-metadata.json](srd121_nist-codata-fundamental-physical-constants-2014-metadata.json) (metadata for CODATA 2014) from https://catalog.data.gov/harvest/object/14b5729a-4814-409b-8e0a-cd733f06b850 downloaded 2 Sep 2018 off https://catalog.data.gov/dataset/nist-codata-fundamental-physical-constants-srd-121.

If anyone finds a JSON/XML/YAML file for the 2nd & 3rd items from NIST or IUPAC, that would be preferable. Or an update to anything.

### January 2020

* The CODATA 2014 JSON file mentioned above is no longer accessible.
* CODATA 2018 has not been published in JSON. Instead, the [build script](https://github.com/MolSSI/QCElemental/blob/master/devtools/scripts/build_physical_constants_2018.py) is working from the published ASCII table at https://physics.nist.gov/cuu/Constants/Table/allascii.txt, a copy of which has been saved here at [codata-2018.txt](codata-2018.txt) downloaded 15 Jan 2020
* Though it is not used in this repository, a counterpart published ASCII table for CODATA 2014 from https://physics.nist.gov/cuu/Constants/Table/allascii_2014.txt has been saved here at [codata-2014.txt](codata-2014.txt) downloaded 15 Jan 2020

If anyone finds a DOI for CODATA 2018, please notify.
