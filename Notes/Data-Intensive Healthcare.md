---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Data-Intensive Healthcare[^1]
> The application of the fourth paradigm to medicine: aggregating an individual's health data from multiple sources, including electronic health records, into unified statistical models to support prediction, prevention, and clinical decision-making.

# Properties
- **Knowledge-translation lag**: the average delay from significant discovery to routine care is about 17 years, only about half of adults receive recommended care, and a single specialist would need about 21 hours of study per day to stay current; instantaneous knowledge flow could speed responses to drug withdrawals and emerging diseases.[^2]
- Medical data remains largely on paper or in disparate formats and silos; sharing is hampered by imperfect de-identification, privacy and sovereignty concerns, and regional, organisational, and provider barriers.[^3]
- Hypothesis-driven, reductionist research identified major independent determinants of health but does not capture its complexity; a unified approach exploits EHR statistics alongside study data ([[Health Avatar]]).[^4]
- **Scale**: systems must *scale out* (across countries, regions, and diseases) and *scale in* (capture and benchmark against a single individual).[^5]
- **Diagnostic decision support**: physicians overestimate their diagnostic accuracy. A [[Bayesian Inference|Bayesian]] reasoning engine (NxKM, built on probabilistic similarity networks) can ask further questions chosen by value-of-information computations, report confidence in the most likely diagnosis, prepopulate location-specific findings, tailor questions to health workers' skill, and down-weight unsubstantiated evidence for data integrity.[^6]
- Global deployment faces device-independent interfaces, literacy (voice recognition or keypad answers), reproducible patient identification (biometrics plus GPS), data volume, and above all cooperation; a connected global health record could enable near-instant detection of outbreaks and drug resistance.[^7]
- An application of [[Data-Intensive Science]].

[^1]: [Hey et al., 2009, p. 96](zotero://open-pdf/library/items/XHD2CC9T?page=130&annotation=YXY874WP); [Hey et al., 2009, p. 94](zotero://open-pdf/library/items/XHD2CC9T?page=128&annotation=5Z6TT995)
[^2]: [Hey et al., 2009, p. 58](zotero://open-pdf/library/items/XHD2CC9T?page=92&annotation=MKITKX26); [Hey et al., 2009, p. 58](zotero://open-pdf/library/items/XHD2CC9T?page=92&annotation=9B4JV5HQ); [Hey et al., 2009, p. 61](zotero://open-pdf/library/items/XHD2CC9T?page=95&annotation=R3S2E9HP); [Hey et al., 2009, p. 62](zotero://open-pdf/library/items/XHD2CC9T?page=96&annotation=MSW6JDQX)
[^3]: [Hey et al., 2009, p. 65](zotero://open-pdf/library/items/XHD2CC9T?page=99&annotation=AVHTH2TL); [Hey et al., 2009, p. 69](zotero://open-pdf/library/items/XHD2CC9T?page=103&annotation=BXIVKZDG); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=FZSLGB2P)
[^4]: [Hey et al., 2009, p. 93](zotero://open-pdf/library/items/XHD2CC9T?page=127&annotation=ZM89SXIH); [Hey et al., 2009, p. 93](zotero://open-pdf/library/items/XHD2CC9T?page=127&annotation=XY8HT39A); [Hey et al., 2009, p. 94](zotero://open-pdf/library/items/XHD2CC9T?page=128&annotation=5Z6TT995)
[^5]: [Hey et al., 2009, p. 66](zotero://open-pdf/library/items/XHD2CC9T?page=100&annotation=H976TKIN); [Hey et al., 2009, p. 66](zotero://open-pdf/library/items/XHD2CC9T?page=100&annotation=64Y8F52R); [Hey et al., 2009, p. 66](zotero://open-pdf/library/items/XHD2CC9T?page=100&annotation=CLVBR4CB); [Hey et al., 2009, p. 67](zotero://open-pdf/library/items/XHD2CC9T?page=101&annotation=QXEFYRMF)
[^6]: [Hey et al., 2009, p. 67](zotero://open-pdf/library/items/XHD2CC9T?page=101&annotation=ZRNPKKEM); [Hey et al., 2009, p. 68](zotero://open-pdf/library/items/XHD2CC9T?page=102&annotation=XTKT8KSY); [Hey et al., 2009, p. 68](zotero://open-pdf/library/items/XHD2CC9T?page=102&annotation=9S8MVAUV); [Hey et al., 2009, p. 69](zotero://open-pdf/library/items/XHD2CC9T?page=103&annotation=CS3FPTX2); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=TX3Z596H); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=5S8GLFBD)
[^7]: [Hey et al., 2009, p. 69](zotero://open-pdf/library/items/XHD2CC9T?page=103&annotation=YBRRAY2M); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=2QJBCFSL); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=97S8F3SR); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=XAK53TGN); [Hey et al., 2009, p. 71](zotero://open-pdf/library/items/XHD2CC9T?page=105&annotation=5QJQW9D6); [Hey et al., 2009, p. 72](zotero://open-pdf/library/items/XHD2CC9T?page=106&annotation=XZ24NYD5); [Hey et al., 2009, p. 72](zotero://open-pdf/library/items/XHD2CC9T?page=106&annotation=KL2H74YH); [Hey et al., 2009, p. 72](zotero://open-pdf/library/items/XHD2CC9T?page=106&annotation=5UNM28MI); [Hey et al., 2009, p. 73](zotero://open-pdf/library/items/XHD2CC9T?page=107&annotation=P5YK3WGQ)
