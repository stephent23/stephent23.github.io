---
type: posts
title: Use of Bespoke Branding in O365 Phishing Campaigns 
tags: [Phishing, Phishing Kits, Obfuscation, JavaScript, Defense Evasion]
category: Phishing
toc: true
---

Phishing campaigns will often use bespoke company branding to make their phishing sites more trustworthy. This post discusses how phishing campaigns are able to dynamically pull the customised branding of organisations that utilise O365. 

## Bespoke Branding
[Microsoft's Documentation](https://docs.microsoft.com/en-us/microsoft-365/admin/setup/customize-sign-in-page?view=o365-worldwide) describes how organisations are able to customise the sign-in pages that users see when they sign-in to Microsoft 365. However, this is also exposed through public Microsoft APIs that adversaries can then leverage to build identical phishing sites. 

## The Phishing Site
Below is a diagram illustrating the requests that are made when an individual browses to a phishing site that is taking advantage of being able to use bespoke branding. 

<div class="mermaid mermaidContainer">
	sequenceDiagram
	Browser->>+Compromised Site: GET /phish?e=[email]
	Compromised Site->>-Browser: phish.html + token
	Browser->>+Microsoft APIs: GET /background?ts=token
	Microsoft APIs->>-Browser: background_image.png
	Browser->>+Microsoft APIs: GET /logo&text?ts=token
	Microsoft APIs->>-Browser: logo.png, text_blurb
</div> 


## The Requests
Analysis of several O365 phishing campaigns that utilised bespoke branding showed that branding was dynamically loaded based upon the email address being phished. These email addresses being targeted are commonly encoded as Base64 in the phishing URL. 

When the phishing link is clicked, the HTML page is returned from the server. The HTML page contains the boiler plate text that would appear on the legitimate O365 sign-in page. Analysing subsequent network requests, there were further calls to the following Microsoft APIs. 
```
https://aadcdn.msauthimages.net/[token_1]/logintenantbranding/0/illustration?ts=[token_2]

https://aadcdn.msauthimages[.]net/[string_identifier1]/logintenantbranding/0/bannerlogo?ts=[token_3]
```
<br />
Information about these URLs is able to be found in [Microsoft's Documentation](https://docs.microsoft.com/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?view=o365-worldwide). These requests were being made with JavaScript that was embedded within the HTML page. These requests loaded the background image and logo used on the legitimate sign-in page for the email address provided. 

However, what wasn't clear is how the adversaries were able to retrieve **`token_1`**, **`token_2`** and **`token_3`** which appeared to be unique for every email address tried. 

## The Tokens
After some research, I came across [this blog](https://o365blog.com/post/desktopsso/) which shows how Microsoft O365 users are able to be enumerated, using the following publicly accessible API: 
```
https://login.microsoftonline.com/common/GetCredentialType
```
<br />
After some experimentation using PowerShell, it proved possible to retrieve the URLs shown above, including the unique identifiers, by making a request to the above Microsoft API. In turn, this enables adversaries to download and display the bespoke O365 branding that the victim would be familiar with on the legitimate sign-in page. This also exposes the boilerplate text that appears on the legitimate login page that the victim usually logs into.

```powershell
$user="user_email@company.com"
$result = Invoke-RestMethod -Uri "https://login.microsoftonline.com/common/GetCredentialType" 
	-ContentType "application/json" -Method POST 
	-Body (@{"username"=$user} | ConvertTo-Json)
$result.EstsProperties.UserTenantBranding
```
<br />
I can't confirm whether this is the API that adversaries are actually using in the backend, although I think it is highly likely. However, bespoke branding undoubtedly provides adversaries with a far greater success rate for their phishing campaigns.