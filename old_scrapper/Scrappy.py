from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

class Scrap:

    def __init__(self, urls, input, output) -> None:
        self.urls = urls
        self.input = input
        self.output = output
    
    def makeCode(self, codeList):
        code = ""
        for i in range(len(codeList)):
            if i != len(codeList) - 1:
                code += codeList[i] + "."
            else:
                code += codeList[i]
        return code

    def getGrade(self, soup):
        grade = ""
        headText = soup.find("h1").text
        head = headText.split(" » ")
        if len(head) > 2:
            grade = head[2][6:] 
        else:
            if(len(head[0]) == 7):
                grade = head[0][6:]
            else:
                grade = head[0]
        return grade

    def getDomain(self, soup):
        head = soup.find("h1").text
        return head.split(" » ")[1]

    def isEla(self, soup):
        return len(soup.find("h1").text.split(" » ")) > 2

    def getSub(self, soup, grade, domain, substandards):
        topics = soup.find_all("h4")
        for topic in topics:
            sib = topic.next_sibling
            while(sib.name != 'h4' and sib.text != "\n" and sib.text != " "):
                if("substandard" in sib['class']):
                        code = ""
                        desc = ""
                        subject = ""
                        for child in sib.children:
                            if(child.name == "a"):
                                codeList = re.split(r'\.', child.text)
                                if self.isEla(soup):
                                    code = self.makeCode(codeList[2:])
                                    subject = codeList[1][0:3]
                                else:
                                    code = self.makeCode(codeList[3:])
                                    subject = codeList[1]
                            else:
                                desc += child.text.strip()
                        substandard = {
                            "Grade": grade,
                            "Subject": subject,
                            "Domain": domain,
                            "Topic": topic.text,
                            "code": code,
                            "desc": desc
                        }
                        substandards.append(substandard)
                if(sib.next_sibling is not None):
                    sib = sib.next_sibling
                else:
                    break
        return substandards

    def scrap(self):
        substandards = []
        for url in self.urls:
            result = requests.get(url)
            doc = BeautifulSoup(result.text, "html.parser")
            grade = self.getGrade(doc)
            domain = self.getDomain(doc)
            substandards = self.getSub(doc, grade, domain, substandards)
        return substandards 

    def writeCSV(self, substandards):
        data = pd.DataFrame(substandards)
        crosswalk = pd.read_csv(self.input)
        print(data)
        frames = [crosswalk, data]
        unite = pd.concat(frames)
        print(unite.to_csv(self.output, mode='w+', index=False))





