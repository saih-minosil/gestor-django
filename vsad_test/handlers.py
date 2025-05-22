import os
import re
import datetime
import xml.sax

dir_xml="vsad_test/xml"

class ObsHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.CurrentTag=""
        self.include=False
        self.Values={}

    def reset(self):
        self.CurrentData = ""
        self.CurrentTag = ""
        self.include = False
        self.Values = {}

    def getValues(self):
        return self.Values

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "series":
            pass
        if tag=='header':
            pass
        if tag == 'parameterId':
            pass
        if tag == 'event':
            if self.include:
                fecha=attributes["date"]+" "+attributes["time"]
                ts=int(datetime.datetime.strptime(fecha,"%Y-%m-%d %H:%M:00").timestamp())
                self.Values[self.CurrentTag][ts]=float(attributes["value"])


    # Call when an elements ends
    def endElement(self, tag):
        if tag == "series":
            self.include=False
            self.CurrentTag = ""
        self.CurrentData = ""


    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "parameterId":
            if content=="Discharge" or content=="Q.obs" or content=="I.obs" or content=="Discharge_forecast":
                self.include=True
                self.CurrentTag=self.CurrentTag+"_"+content
                self.Values[self.CurrentTag]={}


        elif self.CurrentData == "locationId":
            self.CurrentTag = content





