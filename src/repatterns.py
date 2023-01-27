import re

_re_date = (
    r"(?i)(?:[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan\.?|january|feb\.?|february|"
    r"mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|"
    r"september|oct\.?|october|nov\.?|november|dec\.?|december)|(?:jan\.?|january|"
    r"feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|"
    r"august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)\s+[0-3]?"
    r"\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|[0-3]?\d[-\./][0-3]?\d[-\./]\d{2,4}"
)
_re_time = r"(?i)\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?"
_re_phone = (
    r"((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?"
    r"\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*"
    r"\d{3}\s*\d{4}(?![\d-])))"
)
_re_phones_with_exts = (
    r"(?i)(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*(?:[2-9]1[02-9]|[2-9][02-8]1|"
    r"[2-9][02-8][02-9])\s*\)|(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))"
    r"\s*(?:[.-]\s*)?)?(?:[2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})"
    r"\s*(?:[.-]\s*)?(?:[0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(?:\d+)?)"
)
_re_link = (
    r"(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|"
    r"(?:construction)|(?:contractors)|(?:enterprises)|(?:photography)|(?:immobilien)|"
    r"(?:management)|(?:technology)|(?:directory)|(?:education)|(?:equipment)|"
    r"(?:institute)|(?:marketing)|(?:solutions)|(?:builders)|(?:clothing)|"
    r"(?:computer)|(?:democrat)|(?:diamonds)|(?:graphics)|(?:holdings)|(?:lighting)|"
    r"(?:plumbing)|(?:training)|(?:ventures)|(?:academy)|(?:careers)|(?:company)|"
    r"(?:domains)|(?:florist)|(?:gallery)|(?:guitars)|(?:holiday)|(?:kitchen)|"
    r"(?:recipes)|(?:shiksha)|(?:singles)|(?:support)|(?:systems)|(?:agency)|"
    r"(?:berlin)|(?:camera)|(?:center)|(?:coffee)|(?:estate)|(?:kaufen)|(?:luxury)|"
    r"(?:monash)|(?:museum)|(?:photos)|(?:repair)|(?:social)|(?:tattoo)|(?:travel)|"
    r"(?:viajes)|(?:voyage)|(?:build)|(?:cheap)|(?:codes)|(?:dance)|(?:email)|"
    r"(?:glass)|(?:house)|(?:ninja)|(?:photo)|(?:shoes)|(?:solar)|(?:today)|(?:aero)|"
    r"(?:arpa)|(?:asia)|(?:bike)|(?:buzz)|(?:camp)|(?:club)|(?:coop)|(?:farm)|(?:gift)|"
    r"(?:guru)|(?:info)|(?:jobs)|(?:kiwi)|(?:land)|(?:limo)|(?:link)|(?:menu)|(?:mobi)|"
    r"(?:moda)|(?:name)|(?:pics)|(?:pink)|(?:post)|(?:rich)|(?:ruhr)|(?:sexy)|(?:tips)|"
    r"(?:wang)|(?:wien)|(?:zone)|(?:biz)|(?:cab)|(?:cat)|(?:ceo)|(?:com)|"
    r"(?:edu)|(?:gov)|(?:int)|(?:mil)|(?:net)|(?:onl)|(?:org)|(?:pro)|(?:red)|(?:tel)|"
    r"(?:uno)|(?:xxx)|(?:ac)|(?:ad)|(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|"
    r"(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)|(?:ax)|(?:az)|(?:ba)|(?:bb)|"
    r"(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)|"
    r"(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|"
    r"(?:ch)|(?:ci)|(?:ck)|(?:cl)|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|"
    r"(?:cx)|(?:cy)|(?:cz)|(?:de)|(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:dz)|(?:ec)|(?:ee)|"
    r"(?:eg)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|"
    r"(?:ga)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|(?:gm)|(?:gn)|"
    r"(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|"
    r"(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)|(?:iq)|(?:ir)|"
    r"(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|"
    r"(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:lb)|(?:lc)|(?:li)|(?:lk)|"
    r"(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)|(?:ma)|(?:mc)|(?:md)|(?:me)|(?:mg)|"
    r"(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|"
    r"(?:mu)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|"
    r"(?:ni)|(?:nl)|(?:no)|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|"
    r"(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)|(?:ps)|(?:pt)|(?:pw)|(?:py)|"
    r"(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|"
    r"(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:st)|"
    r"(?:su)|(?:sv)|(?:sx)|(?:sy)|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|"
    r"(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|(?:tr)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|"
    r"(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:vg)|(?:vi)|"
    r"(?:vn)|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:za)|(?:zm)|(?:zw))"
    r"(?:/[^\s()<>]+[^\s`!()\[\]{};:'\".,<>?\xab\xbb\u201c\u201d\u2018\u2019])?)"
)
_re_email = (
    r"(?i)([A-Za-z0-9!#$%&'*+\/=?^_{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"
    r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
)
_re_ipv4 = (
    r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]"
    r"[0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|"
    r"[01]?[0-9][0-9]?)"
)
_re_ipv6 = (
    r"\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}"
    r"(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)"
    r"(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|"
    r"[1-9]?\d)){3})\s*"
)
_re_ip_pattern = _re_ipv4 + "|" + _re_ipv6
_re_not_known_ports = (
    r"6[0-5]{2}[0-3][0-5]|[1-5][\d]{4}|[2-9][\d]{3}|1[1-9][\d]{2}|10[3-9][\d]|102[4-9]"
)
_re_price = r"[$]\s?[+-]?[0-9]{1,3}(?:(?:,?[0-9]{3}))*(?:\.[0-9]{1,2})?"
_re_hex_color = "(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})\\b"
_re_credit_card = "((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])"
_re_visa_card = r"4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}"
_re_master_card = r"5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}"
_re_btc_address = (
    "(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])"
)
_re_street_address = (
    r"\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|"
    r"trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)"
)
_re_zip_code = r"\b\d{5}(?:[-\s]\d{4})?\b"
_re_po_box = r"(?i)P\.? ?O\.? Box \d+"
_re_ssn = r"(?:\d{3}-\d{2}-\d{4})"
_re_md5_hashes = r"[0-9a-fA-F]{32}"
_re_sha1_hashes = r"[0-9a-fA-F]{40}"
_re_sha256_hashes = r"[0-9a-fA-F]{64}"
_re_isbn13 = r"(?:[\d]-?){12}[\dxX]"
_re_isbn10 = r"(?:[\d]-?){9}[\dxX]"
_re_mac_address = r"(([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2}))"
_re_iban_by_country = (
    r"AL[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{4}[\s-]?){4}",
    r"AD[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{4}[\s-]?){3}",
    r"AT[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"AZ[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}",
    r"BH[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){3}"
    r"(?:[a-zA-Z0-9]{2})",
    r"BY[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}",
    r"BE[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}",
    r"BA[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"BR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{3})(?:[a-zA-Z]{1}[\s-]?)"
    r"(?:[a-zA-Z0-9]{1})",
    r"BG[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){1}(?:[0-9]{2})"
    r"(?:[a-zA-Z0-9]{2}[\s-]?)(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[a-zA-Z0-9]{2})",
    r"CR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"HR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{1})",
    r"CY[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{4}[\s-]?){4}",
    r"CZ[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"DK[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"DO[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}",
    r"TL[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{3})",
    r"EE[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"FO[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"FI[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"FR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})(?:[a-zA-Z0-9]{2}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{1})(?:[0-9]{2})",
    r"GE[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{2})(?:[0-9]{2}[\s-]?)(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{2})",
    r"DE[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"GI[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){3}"
    r"(?:[a-zA-Z0-9]{3})",
    r"GR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{3})(?:[a-zA-Z0-9]{1}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){3}(?:[a-zA-Z0-9]{3})",
    r"GL[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"GT[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){5}",
    r"HU[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){6}",
    r"IS[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{2})",
    r"IE[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{2})",
    r"IL[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{3})",
    r"IT[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{1})(?:[0-9]{3}[\s-]?)(?:[0-9]{4}"
    r"[\s-]?){1}(?:[0-9]{3})"
    r"(?:[a-zA-Z0-9]{1}[\s-]?)(?:[a-zA-Z0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{3})",
    r"JO[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}(?:[0-9]{2})",
    r"KZ[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{1})(?:[a-zA-Z0-9]{3}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{2})",
    r"XK[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})"
    r"(?:[0-9]{2}[\s-]?)",
    r"KW[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){5}"
    r"(?:[a-zA-Z0-9]{2})",
    r"LV[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){3}"
    r"(?:[a-zA-Z0-9]{1})",
    r"LB[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){5}",
    r"LI[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})(?:[a-zA-Z0-9]{3}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{1})",
    r"LT[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"LU[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{3})(?:[a-zA-Z0-9]{1}[\s-]?)(?:[a-zA-Z0-9]{4}"
    r"[\s-]?){3}",
    r"MK[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{3})(?:[a-zA-Z0-9]{1}[\s-]?)(?:[a-zA-Z0-9]{4}"
    r"[\s-]?){2}(?:[a-zA-Z0-9]{1})(?:[0-9]{2})",
    r"MT[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})"
    r"(?:[a-zA-Z0-9]{3}[\s-]?)(?:[a-zA-Z0-9]{4}[\s-]?){3}(?:[a-zA-Z0-9]{3})",
    r"MR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{3})",
    r"MU[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){4}(?:[0-9]{3})"
    r"(?:[a-zA-Z]{1}[\s-]?)(?:[a-zA-Z]{2})",
    r"MC[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})(?:[a-zA-Z0-9]{2}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{1})(?:[0-9]{2})",
    r"MD[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{2})(?:[a-zA-Z0-9]{2}[\s-]?)(?:[a-zA-Z0-9]{4}"
    r"[\s-]?){4}",
    r"ME[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"NL[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})",
    r"NO[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[0-9]{3})",
    r"PK[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){4}",
    r"PS[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}"
    r"(?:[0-9]{1})",
    r"PL[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){6}",
    r"PT[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{1})",
    r"QA[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){5}"
    r"(?:[a-zA-Z0-9]{1})",
    r"RO[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[a-zA-Z0-9]{4}[\s-]?){4}",
    r"SM[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{1})(?:[0-9]{3}[\s-]?)(?:[0-9]{4}[\s-]?){1}"
    r"(?:[0-9]{3})(?:[a-zA-Z0-9]{1}[\s-]?)(?:[a-zA-Z0-9]{4}[\s-]?){2}"
    r"(?:[a-zA-Z0-9]{3})",
    r"SA[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{2})(?:[a-zA-Z0-9]{2}[\s-]?)(?:[a-zA-Z0-9]{4}"
    r"[\s-]?){4}",
    r"RS[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"SK[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"SI[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{3})",
    r"ES[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"SE[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"CH[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})(?:[a-zA-Z0-9]{3}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){2}(?:[a-zA-Z0-9]{1})",
    r"TN[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"TR[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})(?:[a-zA-Z0-9]{3}[\s-]?)"
    r"(?:[a-zA-Z0-9]{4}[\s-]?){3}(?:[a-zA-Z0-9]{2})",
    r"AE[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{3})(?:[0-9]{1}[\s-]?)(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{3})",
    r"GB[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"VA[a-zA-Z0-9]{2}[\s-]?(?:[0-9]{3})(?:[0-9]{1}[\s-]?)(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{2})",
    r"VG[a-zA-Z0-9]{2}[\s-]?(?:[a-zA-Z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){4}",
)
_re_iban_number = "|".join(f"(?:{pattern})" for pattern in _re_iban_by_country)
_re_bic_code = r"(?:[a-zA-Z]{4})(?:[a-zA-Z]{2})(?:[a-zA-Z0-9]{2})(?:[a-zA-Z0-9]{3})?"
_re_git_repo = (
    r"((git|ssh|http(s)?)|(git@[\w\.]+))(:(\/\/)?)([\w\.@\:/\-~]+)(\.git)(\/)?"
)


_regex_map = {
    "dates": re.compile(_re_date),
    "times": re.compile(_re_time),
    "phones": re.compile(_re_phone),
    "phones_with_exts": re.compile(_re_phones_with_exts),
    "emails": re.compile(_re_email),
    "links": re.compile(_re_link),
    "ipv4": re.compile(_re_ipv4),
    "ipv6": re.compile(_re_ipv6),
    "ips": re.compile(_re_ip_pattern),
    "not_known_ports": re.compile(_re_not_known_ports),
    "prices": re.compile(_re_price),
    "hex_colors": re.compile(_re_hex_color),
    "credit_cards": re.compile(_re_credit_card),
    "visa_cards": re.compile(_re_visa_card),
    "master_cards": re.compile(_re_master_card),
    "btc_addresses": re.compile(_re_btc_address),
    "street_addresses": re.compile(_re_street_address),
    "zip_codes": re.compile(_re_zip_code),
    "po_boxes": re.compile(_re_po_box),
    "ssn_number": re.compile(_re_ssn),
    "md5_hashes": re.compile(_re_md5_hashes),
    "sha1_hashes": re.compile(_re_sha1_hashes),
    "sha256_hashes": re.compile(_re_sha256_hashes),
    "isbn13": re.compile(_re_isbn13),
    "isbn10": re.compile(_re_isbn10),
    "mac_addresses": re.compile(_re_mac_address),
    "iban_numbers": re.compile(_re_iban_number),
    "bic_codes": re.compile(_re_bic_code),
    # "bic_codes": re.compile(f"\\b{_re_bic_code}\\b"),
    "git_repos": re.compile(_re_git_repo),
}
print(_re_iban_number)


def _match(text: str, regex: re.Pattern) -> list:
    """Function to match using regex findall function
    Args:
        textchunk (str) : textchunk to be supplied to identify pattern
        regex (str) : regex to be used to match
    Returns:
        list (list): list of sensitive data found in lines
    """
    parsed = list(regex.findall(text))
    return parsed


def _match_by_regex_search(text: str, regex: re.Pattern) -> list:
    """Function to match using regex search function
    Args:
        textchunk (str) : textchunk to be supplied to identify pattern
        regex (str) : regex to be used to match
    Returns:
        list (list): list of sensitive data found in lines
    """
    parsed = []
    for line in text.split():
        if regex.search(line):
            pattern_string = re.search(regex, line)
            sensitive_string = pattern_string.group(0)
            parsed.append(sensitive_string)
    return parsed


def dates(text: str) -> list:
    return _match(text, _regex_map["dates"])


def times(text: str) -> list:
    return _match(text, _regex_map["times"])


def phones(text: str) -> list:
    return _match(text, _regex_map["phones"])


def phones_with_exts(text: str) -> list:
    return _match(text, _regex_map["phones_with_exts"])


def emails(text: str) -> list:
    return _match(text, _regex_map["emails"])


def links(text: str) -> list:
    return _match_by_regex_search(text, _regex_map["links"])


def ipv4s(text: str) -> list:
    return _match(text, _regex_map["ipv4"])


def ipv6s(text: str) -> list:
    return _match(text, _regex_map["ipv6"])


def ips(text: str) -> list:
    return _match(text, _regex_map["ips"])


def not_known_ports(text: str) -> list:
    return _match(text, _regex_map["not_known_ports"])


def prices(text: str) -> list:
    return _match(text, _regex_map["prices"])


def hex_colors(text: str) -> list:
    return _match(text, _regex_map["hex_colors"])


def credit_cards(text: str) -> list:
    return _match(text, _regex_map["credit_cards"])


def visa_cards(text: str) -> list:
    return _match(text, _regex_map["visa_cards"])


def master_cards(text: str) -> list:
    return _match(text, _regex_map["master_cards"])


def btc_address(text: str) -> list:
    return _match(text, _regex_map["btc_addresses"])


def street_addresses(text: str) -> list:
    return _match(text, _regex_map["street_addresses"])


def zip_codes(text: str) -> list:
    return _match(text, _regex_map["zip_codes"])


def po_boxes(text: str) -> list:
    return _match(text, _regex_map["po_boxes"])


def ssn_numbers(text: str) -> list:
    return _match(text, _regex_map["ssn_number"])


def md5_hashes(text: str) -> list:
    return _match(text, _regex_map["md5_hashes"])


def sha1_hashes(text: str) -> list:
    return _match(text, _regex_map["sha1_hashes"])


def sha256_hashes(text: str) -> list:
    return _match(text, _regex_map["sha256_hashes"])


def isbn13s(text: str) -> list:
    return _match(text, _regex_map["isbn13"])


def isbn10s(text: str) -> list:
    return _match(text, _regex_map["isbn10"])


def mac_addresses(text: str) -> list:
    return _match_by_regex_search(text, _regex_map["mac_addresses"])


def iban_numbers(text: str) -> list:
    return _match(text, _regex_map["iban_numbers"])


def bic_codes(text: str) -> list:
    return _match(text, _regex_map["bic_codes"])


def git_repos(text: str) -> list:
    return _match_by_regex_search(text, _regex_map["git_repos"])
