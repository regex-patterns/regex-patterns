import re

_re_date = (
    r"(?:[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?"
    r"(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|"
    r"may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|"
    r"nov\.?|november|dec\.?|december)|"
    r"(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|"
    r"may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|"
    r"nov\.?|november|dec\.?|december)"
    r"\s+[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|"
    r"[0-3]?\d[-\./][0-3]?\d[-\./]\d{2,4}"
)

_re_time = r"\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?"

_re_phone = (
    r"(?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?"
    r"\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|"
    r"(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-]))"
)

_re_phones_with_exts = (
    r"(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*(?:[2-9]1[02-9]|[2-9][02-8]1|"
    r"[2-9][02-8][02-9])\s*\)|(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))"
    r"\s*(?:[.-]\s*)?)?(?:[2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})"
    r"\s*(?:[.-]\s*)?(?:[0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(?:\d+)?)"
)

_re_link = (
    r"((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|"
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
    r"([A-Za-z0-9!#$%&'*+\/=?^_{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+"
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
_re_hex_color = "(#(?:[0-9a-fA-F]{8})|#(?:[0-9a-fA-F]{3}){1,2})"
_re_credit_card = r"((?:(?:\d{4}[- ]?){3}\d{4}|\d{15,16}))(?![\d])"
_re_visa_card = r"4\d{3}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}"
_re_master_card = r"5[1-5]\d{2}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}"
_re_btc_address = (
    "(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])"
)
_re_street_address = (
    r"\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|"
    r"trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?"
)
_re_zip_code = r"\d{5}(?:[-\s]\d{4})?"
_re_po_box = r"P\.? ?O\.? Box \d+"
_re_ssn = r"(?:\d{3}-\d{2}-\d{4})"
_re_md5_hashes = r"[0-9a-fA-F]{32}"
_re_sha1_hashes = r"[0-9a-fA-F]{40}"
_re_sha256_hashes = r"[0-9a-fA-F]{64}"
_re_isbn13 = r"(?:[\d]-?){12}[\dxX]"
_re_isbn10 = r"(?:[\d]-?){9}[\dxX]"
_re_mac_address = r"(([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2}))"
_re_iban_by_country = (
    r"AL[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[a-z0-9]{4}[\s-]?){4}",
    r"AD[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[a-z0-9]{4}[\s-]?){3}",
    r"AT[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"AZ[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}",
    r"BH[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){3}(?:[a-z0-9]{2})",
    r"BY[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}",
    r"BE[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}",
    r"BA[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"BR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{3})(?:[a-z]{1}[\s-]?)"
    r"(?:[a-z0-9]{1})",
    r"BG[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){1}(?:[0-9]{2})"
    r"(?:[a-z0-9]{2}[\s-]?)(?:[a-z0-9]{4}[\s-]?){1}(?:[a-z0-9]{2})",
    r"CR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"HR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{1})",
    r"CY[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[a-z0-9]{4}[\s-]?){4}",
    r"CZ[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"DK[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"DO[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}",
    r"TL[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{3})",
    r"EE[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"FO[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"FI[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"FR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})(?:[a-z0-9]{2}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{1})(?:[0-9]{2})",
    r"GE[a-z0-9]{2}[\s-]?(?:[a-z0-9]{2})(?:[0-9]{2}[\s-]?)(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{2})",
    r"DE[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"GI[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){3}(?:[a-z0-9]{3})",
    r"GR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{3})(?:[a-z0-9]{1}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){3}(?:[a-z0-9]{3})",
    r"GL[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"GT[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){5}",
    r"HU[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){6}",
    r"IS[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{2})",
    r"IE[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"IL[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{3})",
    r"IT[a-z0-9]{2}[\s-]?(?:[a-z]{1})(?:[0-9]{3}[\s-]?)(?:[0-9]{4}[\s-]?){1}"
    r"(?:[0-9]{3})(?:[a-z0-9]{1}[\s-]?)(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{3})",
    r"JO[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}(?:[0-9]{2})",
    r"KZ[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{1})(?:[a-z0-9]{3}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{2})",
    r"XK[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})"
    r"(?:[0-9]{2}[\s-]?)",
    r"KW[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){5}(?:[a-z0-9]{2})",
    r"LV[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){3}(?:[a-z0-9]{1})",
    r"LB[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){5}",
    r"LI[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})(?:[a-z0-9]{3}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{1})",
    r"LT[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}",
    r"LU[a-z0-9]{2}[\s-]?(?:[0-9]{3})(?:[a-z0-9]{1}[\s-]?)(?:[a-z0-9]{4}[\s-]?){3}",
    r"MK[a-z0-9]{2}[\s-]?(?:[0-9]{3})(?:[a-z0-9]{1}[\s-]?)(?:[a-z0-9]{4}"
    r"[\s-]?){2}(?:[a-z0-9]{1})(?:[0-9]{2})",
    r"MT[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})"
    r"(?:[a-z0-9]{3}[\s-]?)(?:[a-z0-9]{4}[\s-]?){3}(?:[a-z0-9]{3})",
    r"MR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{3})",
    r"MU[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){4}(?:[0-9]{3})"
    r"(?:[a-z]{1}[\s-]?)(?:[a-z]{2})",
    r"MC[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})(?:[a-z0-9]{2}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{1})(?:[0-9]{2})",
    r"MD[a-z0-9]{2}[\s-]?(?:[a-z0-9]{2})(?:[a-z0-9]{2}[\s-]?)(?:[a-z0-9]{4}"
    r"[\s-]?){4}",
    r"ME[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"NL[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){2}(?:[0-9]{2})",
    r"NO[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){2}(?:[0-9]{3})",
    r"PK[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){4}",
    r"PS[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){5}(?:[0-9]{1})",
    r"PL[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){6}",
    r"PT[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}(?:[0-9]{1})",
    r"QA[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){5}(?:[a-z0-9]{1})",
    r"RO[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[a-z0-9]{4}[\s-]?){4}",
    r"SM[a-z0-9]{2}[\s-]?(?:[a-z]{1})(?:[0-9]{3}[\s-]?)(?:[0-9]{4}[\s-]?){1}"
    r"(?:[0-9]{3})(?:[a-z0-9]{1}[\s-]?)(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{3})",
    r"SA[a-z0-9]{2}[\s-]?(?:[0-9]{2})(?:[a-z0-9]{2}[\s-]?)(?:[a-z0-9]{4}[\s-]?){4}",
    r"RS[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){4}(?:[0-9]{2})",
    r"SK[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"SI[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){3}(?:[0-9]{3})",
    r"ES[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"SE[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"CH[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})(?:[a-z0-9]{3}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){2}(?:[a-z0-9]{1})",
    r"TN[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){5}",
    r"TR[a-z0-9]{2}[\s-]?(?:[0-9]{4}[\s-]?){1}(?:[0-9]{1})(?:[a-z0-9]{3}[\s-]?)"
    r"(?:[a-z0-9]{4}[\s-]?){3}(?:[a-z0-9]{2})",
    r"AE[a-z0-9]{2}[\s-]?(?:[0-9]{3})(?:[0-9]{1}[\s-]?)(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{3})",
    r"GB[a-z0-9]{2}[\s-]?(?:[a-z]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){3}(?:[0-9]{2})",
    r"VA[a-z0-9]{2}[\s-]?(?:[0-9]{3})(?:[0-9]{1}[\s-]?)(?:[0-9]{4}[\s-]?){3}"
    r"(?:[0-9]{2})",
    r"VG[a-z0-9]{2}[\s-]?(?:[a-z0-9]{4}[\s-]?){1}(?:[0-9]{4}[\s-]?){4}",
)
_re_iban_number = "|".join(f"(?:{pattern})" for pattern in _re_iban_by_country)
_re_git_repo = (
    r"((git|ssh|http(s)?)|(git@[\w\.]+))(:(\/\/)?)([\w\.@\:/\-~]+)(\.git)(\/)?"
)


class RegexPatterns:
    """Main class used to match patterns."""

    def __init__(self, case_sensitive=False, check_word_boundaries=False) -> None:
        """Initialize the class.

        Args:
            case_sensitive: When set to True, indicates that the case should be
                considered by the regex matcher.
            check_word_boundaries: When set to True, only considers matches where the
                boundaries are not alpha numeric charactes.
        """
        self.case_sensitive = case_sensitive
        self.check_word_boundaries = check_word_boundaries
        self.regex_map = {
            "dates": self._compile(_re_date),
            "times": self._compile(_re_time),
            "phones": self._compile(_re_phone),
            "phones_with_exts": self._compile(_re_phones_with_exts),
            "emails": self._compile(_re_email),
            "links": self._compile(_re_link),
            "ipv4": self._compile(_re_ipv4),
            "ipv6": self._compile(_re_ipv6),
            "ips": self._compile(_re_ip_pattern),
            "not_known_ports": self._compile(_re_not_known_ports),
            "prices": self._compile(_re_price),
            "hex_colors": self._compile(_re_hex_color),
            "credit_cards": self._compile(_re_credit_card),
            "visa_cards": self._compile(_re_visa_card),
            "master_cards": self._compile(_re_master_card),
            "btc_addresses": self._compile(_re_btc_address),
            "street_addresses": self._compile(_re_street_address),
            "zip_codes": self._compile(_re_zip_code),
            "po_boxes": self._compile(_re_po_box),
            "ssn_number": self._compile(_re_ssn),
            "md5_hashes": self._compile(_re_md5_hashes),
            "sha1_hashes": self._compile(_re_sha1_hashes),
            "sha256_hashes": self._compile(_re_sha256_hashes),
            "isbn13": self._compile(_re_isbn13),
            "isbn10": self._compile(_re_isbn10),
            "mac_addresses": self._compile(_re_mac_address),
            "iban_numbers": self._compile(_re_iban_number),
            "git_repos": self._compile(_re_git_repo),
        }

    def _compile(self, re_pattern: str):
        """Internal method used to compile the regex patterns.

        Args:
            re_pattern: Regex patter passed to `re.compile`.

        Returns:
            Compiled regex.
        """
        if self.check_word_boundaries:
            re_pattern = re_pattern
        if self.case_sensitive:
            return re.compile(re_pattern)
        else:
            return re.compile(re_pattern, flags=re.IGNORECASE)

    def match(self, text: str, regex: re.Pattern) -> list:
        """Function to match using regex findall function
        Args:
            textchunk (str) : textchunk to be supplied to identify pattern
            regex (str) : regex to be used to match
        Returns:
            list (list): list of sensitive data found in lines
        """
        if self.check_word_boundaries:
            list_matches = []
            for match in regex.finditer(text):
                if match.start() == 0 or not text[match.start()].isalnum():
                    if match.end() == len(text) or not text[match.end()].isalnum():
                        list_matches.append(match.group())
        else:
            list_matches = list(regex.findall(text))
        return list_matches

    def match_by_regex_search(self, text: str, regex: re.Pattern) -> list:
        """Function to match using regex search function
        Args:
            textchunk (str) : textchunk to be supplied to identify pattern
            regex (str) : regex to be used to match
        Returns:
            list (list): list of sensitive data found in lines
        """
        parsed = []
        for line in text.split():
            match = regex.search(line)
            if match:
                sensitive_string = match.group(0)
                parsed.append(sensitive_string)
        return parsed

    def dates(self, text: str) -> list:
        return self.match(text, self.regex_map["dates"])

    def times(self, text: str) -> list:
        return self.match(text, self.regex_map["times"])

    def phones(self, text: str) -> list:
        return self.match(text, self.regex_map["phones"])

    def phones_with_exts(self, text: str) -> list:
        return self.match(text, self.regex_map["phones_with_exts"])

    def emails(self, text: str) -> list:
        return self.match(text, self.regex_map["emails"])

    def links(self, text: str) -> list:
        return self.match_by_regex_search(text, self.regex_map["links"])

    def ipv4s(self, text: str) -> list:
        return self.match(text, self.regex_map["ipv4"])

    def ipv6s(self, text: str) -> list:
        return self.match(text, self.regex_map["ipv6"])

    def ips(self, text: str) -> list:
        return self.match(text, self.regex_map["ips"])

    def not_known_ports(self, text: str) -> list:
        return self.match(text, self.regex_map["not_known_ports"])

    def prices(self, text: str) -> list:
        return self.match(text, self.regex_map["prices"])

    def hex_colors(self, text: str) -> list:
        return self.match(text, self.regex_map["hex_colors"])

    def credit_cards(self, text: str) -> list:
        return self.match(text, self.regex_map["credit_cards"])

    def visa_cards(self, text: str) -> list:
        return self.match(text, self.regex_map["visa_cards"])

    def master_cards(self, text: str) -> list:
        return self.match(text, self.regex_map["master_cards"])

    def btc_address(self, text: str) -> list:
        return self.match(text, self.regex_map["btc_addresses"])

    def street_addresses(self, text: str) -> list:
        return self.match(text, self.regex_map["street_addresses"])

    def zip_codes(self, text: str) -> list:
        return self.match(text, self.regex_map["zip_codes"])

    def po_boxes(self, text: str) -> list:
        return self.match(text, self.regex_map["po_boxes"])

    def ssn_numbers(self, text: str) -> list:
        return self.match(text, self.regex_map["ssn_number"])

    def md5_hashes(self, text: str) -> list:
        return self.match(text, self.regex_map["md5_hashes"])

    def sha1_hashes(self, text: str) -> list:
        return self.match(text, self.regex_map["sha1_hashes"])

    def sha256_hashes(self, text: str) -> list:
        return self.match(text, self.regex_map["sha256_hashes"])

    def isbn13s(self, text: str) -> list:
        return self.match(text, self.regex_map["isbn13"])

    def isbn10s(self, text: str) -> list:
        return self.match(text, self.regex_map["isbn10"])

    def mac_addresses(self, text: str) -> list:
        return self.match_by_regex_search(text, self.regex_map["mac_addresses"])

    def iban_numbers(self, text: str) -> list:
        return self.match(text, self.regex_map["iban_numbers"])

    def git_repos(self, text: str) -> list:
        return self.match_by_regex_search(text, self.regex_map["git_repos"])
