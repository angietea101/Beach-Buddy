"""
CECS 323 Version 1
"""

import requests

url = "https://cmsweb.cms.csulb.edu/psc/CLBPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL"

payload = 'ICAJAX=1&ICNAVTYPEDROPDOWN=0&ICType=Panel&ICElementNum=0&ICStateNum=13&ICAction=CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH&_gs_page=SSR_CLSRCH_ENTRY&_gs_cs=DERIVED_CLSRCH_SSR_EXPAND_COLLAPS%24149%24%240&ICModelCancel=0&ICXPos=0&ICYPos=254&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICSkipPending=0&ICAutoSave=0&ICResubmit=0&ICSID=UFt5M4gBI6fJjFdqDGoAbayyQvAjAtWP7tNylIJW5zE%3D&ICActionPrompt=false&ICBcDomData=UnknownValue&ICPanelName=&ICFind=&ICAddCount=&ICAppClsData=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO%2427%24=&SSR_CLSRCH_WRK_SUBJECT_SRCH%240=CECS&SSR_CLSRCH_WRK_SSR_EXACT_MATCH1%241=E&SSR_CLSRCH_WRK_CATALOG_NBR%241=323&SSR_CLSRCH_WRK_ACAD_CAREER%242=&SSR_CLSRCH_WRK_INSTRUCTION_MODE%243=&SSR_CLSRCH_WRK_SSR_OPEN_ONLY%24chk%244=N'
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'PS_TokenSite=https://cmsweb.cms.csulb.edu/psc/CLBPRD/?CLBPRD-PSJSESSIONID; SignOnDefault=; _gid=GA1.2.425392029.1713305064; _ga_W3BGL1LGZT=GS1.1.1713326248.8.0.1713326250.58.0.0; CLBPRD-PSJSESSIONID=sFHqNDQ-9B8mFmjXnruumHp83h59yzJk!-244380455; ExpirePage=https://cmsweb.cms.csulb.edu/psc/CLBPRD/; PS_LOGINLIST=https://cmsweb.cms.csulb.edu/CLBPRD; PS_TOKEN=ogAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AcQg4AC4AMQAwABSmts4X03hd4aFxtX4gZPl4So5hlWIAAAAFAFNkYXRhVnicHYtLDkBAEAXLECsr9yCMMWbtExsRcRP3czivdSdVvah+gCJ3WSa/jn/qDk9iYCLKUVtunOxUCwczFzcrwWNhoJGNvULjQMuoZ6PdXrYiiXxmWgsR; PS_LASTSITE=https://cmsweb.cms.csulb.edu/psc/CLBPRD/; PS_DEVICEFEATURES=width:1920 height:1080 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; _ga=GA1.1.2139290475.1705914360; _ga_73K73VXG78=GS1.2.1713326276.6.1.1713326281.0.0.0; psback=%22%22url%22%3A%22https%3A%2F%2Fcmsweb.cms.csulb.edu%2Fpsc%2FCLBPRD%2FEMPLOYEE%2FSA%2Fc%2FSA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL%3FPage%3DSSR_SSENRL_CART%26Action%3DA%26ACAD_CAREER%3DUGRD%26EMPLID%3D028376866%26INSTITUTION%3DLBCMP%26STRM%3D2244%22%20%22label%22%3A%22Enrollment%20Shopping%20Cart%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%20%22refurl%22%3A%22https%3A%2F%2Fcmsweb.cms.csulb.edu%2Fpsc%2FCLBPRD%2FEMPLOYEE%2FSA%22%22; _ga_W6HQD1GGLJ=GS1.1.1713326276.6.1.1713326288.0.0.0; AWSALB=IK5+2aD3S+B1C8D2DSfs4EGEfipLHR54rdbdNZCBezga5XDKD76p8bJj7HDcyfDdEy+3uRZkaRHwg7G4xsvKVWZhxsW6tq/Yhh3ly2qMRfgHUhjv8vrTZSbrQANa; AWSALBCORS=IK5+2aD3S+B1C8D2DSfs4EGEfipLHR54rdbdNZCBezga5XDKD76p8bJj7HDcyfDdEy+3uRZkaRHwg7G4xsvKVWZhxsW6tq/Yhh3ly2qMRfgHUhjv8vrTZSbrQANa; PS_TOKENEXPIRE=17_Apr_2024_04:04:59_GMT; PS_LASTSITE=https://cmsweb.cms.csulb.edu/psc/CLBPRD/; PS_TOKENEXPIRE=17_Apr_2024_04:05:17_GMT; AWSALB=NFn3VYARzg9MICsgB6KSD6sM9pmf8U0bY+yazibaGW+VCaue2Q4yl8trPydFMCiuKPIU20KEYL8kvxRtchFQWwO4w8FgzyQYO17Bs9E8bJJRh7YpmNUIbNDm20AG; AWSALBCORS=NFn3VYARzg9MICsgB6KSD6sM9pmf8U0bY+yazibaGW+VCaue2Q4yl8trPydFMCiuKPIU20KEYL8kvxRtchFQWwO4w8FgzyQYO17Bs9E8bJJRh7YpmNUIbNDm20AG',
  'origin': 'https://cmsweb.cms.csulb.edu',
  'referer': 'https://cmsweb.cms.csulb.edu/psc/CLBPRD/EMPLOYEE/SA/c/SA_LEARNER_SERVICES_2.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=028376866&INSTITUTION=LBCMP&STRM=2244',
  'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
