# Project Scope Document 

---

## 1. Project Overview
**Project Name:** PDF Auditor<br>
**Prepared By:** Liam Slade<br>
**Date:** 07-30-2025

## 1.1 Purpose 
The PDF Auditor exists to give accessibility teams and website owners an easy-to-use desktop tool that automates end-to-end compliance checks on PDFs published on any public website. It combines web scraping, PDF retreival, and standard-based accessibility analysis all into a single GUI.

## 1.2 Background 
During my time at archSCAN LLC, I took lead on promoting and demonstrating one of our new services: Accessibility-on-Demand (AoD). This on-demand service provided a much more cost effective and time efficient way to remediate documents by utilizing artificial intelligence, machine learning, and computer vision. One of the ways I went about promoting and demonstrating this service was when we had a lead/potential client, I would grab any public facing documentation from their organization's website and check for compliance (any documentation that I would find to be non-compliant would then be used in demonstrating AoD). When doing so, I found that manually going through a website and downloading every PDF I found was very time-consuming and inefficient.  

## 2. Objectives 
This solution serves to:<br> 
    1. Discover all publicly-linked PDF documents on a target site via webscraping.<br> 
    2. Retrieve and download those PDFs to a specified directory.<br>
    3. Analyze each PDF for key accessibility criteria (PDF/UA and WCAG 2.1).<br> 
    4. Report results into an Excel workbook that which documents passed and failed.<br>

All within a time-efficient manner and presented in a user-friendly GUI

## 3 Deliverables

| Deliverable                | Description                                                                | Due Date             | Status          |
|:---------------------------|:---------------------------------------------------------------------------|:--------------------:|:---------------:|
| Project Scope Document | A Markdown file that defines the projects purpose, background, objectives, deliverables, milestones, in-scope and out-of-scope featuers, functional and non-functional requirements, assumptions, constraints, risk & mitigation plans, and stakeholders. | TBD | Pending Review |
| Technical Requirements Specifications | A detailed spec outlining data inputs/outputs, performance targets, and compliance standards. | TBD | In Progress |
| Web Scraper Module | Component to discover and retrieve all publicly-linked PDFs from a target website. | TBD | Not started |
| Accessibility Analysis Engine | Module to analyze PDFs for PDF/UA and WCAG 2.1 compliance. | TBD | Not started |
| GUI Application | User-friendly desktop interface integrating all modules and workflows. | TBD | Not started |
| Reporting System | Generates Excel reports summarizing compliance results for all analyzed PDFs. | TBD | Not started |
| User Documentation | Guides for installation, usage, troubleshooting, and support. | TBD | Not started |

# 4. Milestones
| Milestone                  | Target Date   | Owner         |
|----------------------------|---------------|---------------|
 | Project Scope & Planning Complete      | TBD | Liam Slade      |
 | Technical Requirements Finalized       | TBD | Liam Slade      |
 | Web Scraper Module Developed           | TBD | Liam Slade      |
 | Accessibility Analysis Engine Complete | TBD | Liam Slade      |
 | GUI Prototype Ready                    | TBD | Liam Slade      |
 | Reporting System Implemented           | TBD | Liam Slade      |
 | User Documentation Drafted             | TBD | Liam Slade      |
 | QA & Testing Complete                  | TBD | Liam Slade      |
 | Final Release                          | TBD | Liam Slade      |

## 5. Scope Description 

## 5.1 In Scope
 - Automated discovery of publicly-linked PDF documents on target websites
 - Downloading and local storage of discovered PDFs
 - Accessibility analysis of PDFs for PDF/UA and WCAG 2.1 compliance
 - Generation of Excel reports summarizing compliance results
 - User-friendly desktop GUI for all major workflows
 - User documentation (installation, usage, troubleshooting)
 - Automated and manual testing of all major features

## 5.2 Out of Scope
 - Remediation or editing of PDF content for compliance
 - Accessibility analysis of non-PDF file formats
 - Web-based/cloud deployment of the application
 - Integration with third-party document management systems
 - Real-time monitoring of website changes
 - Support for mobile platforms

## 6. Requirements 

## 6.1 Functional Requirements
 - The system shall discover all publicly-linked PDF documents on a specified website via web scraping.
 - The system shall download and store discovered PDFs in a user-specified local directory.
 - The system shall analyze each PDF for compliance with PDF/UA and WCAG 2.1 accessibility standards.
 - The system shall generate an Excel report summarizing the compliance results for each PDF.
 - The system shall provide a graphical user interface (GUI) for initiating scans, viewing results, and exporting reports.
 - The system shall allow users to configure scan parameters (e.g., target URL, output directory).
 - The system shall provide user documentation for installation, usage, and troubleshooting.
 - The system shall include automated and manual tests for all major features.

## 6.2 Non-Functional Requirements
 - The system shall complete PDF discovery, download, and analysis for a typical website (up to 100 PDFs) within 30 minutes.
 - The system shall support Windows 10 and above.
 - The system shall provide clear error messages and logging for failed operations.
 - The system shall ensure user data privacy and not transmit PDFs or results externally.
 - The system shall be maintainable and modular for future feature additions.
 - The system shall have a user-friendly and accessible GUI (meeting WCAG 2.1 AA for software interfaces).
 - The system shall require minimal installation steps and dependencies.

## 7 Assuptions & Constraints
## 7.1 Assumptions
 - Target websites have publicly accessible PDF links that can be discovered via web scraping.
 - Users have the necessary permissions to download and analyze PDFs from target websites.
 - The majority of target PDFs are not password-protected or encrypted.
 - Users will operate the application on supported Windows environments.
 - Internet connectivity is available during PDF discovery and download.
 - Users will provide accurate URLs and output directories.

## 7.2 Constraints
 - The application is limited to Windows 10 and above.
 - Only publicly accessible, non-password-protected PDFs can be analyzed.
 - The system does not modify or remediate PDF content.
 - The application does not support real-time website monitoring or cloud deployment.
 - Maximum recommended website size for analysis is 100 PDFs per scan.
 - The application must comply with relevant data privacy regulations (e.g., GDPR).

## 8. Risk & Mitigation
| Risk                        | Probability    | Impact         | Mitigation Plan              |
|-----------------------------|----------------|----------------|------------------------------|
| Incomplete PDF discovery due to website structure changes | Medium | High | Regularly update and test web scraping logic; allow user feedback for missed files. |
| Download failures or inaccessible PDFs | Medium | Medium | Implement robust error handling and retry logic; log failures for user review. |
| False positives/negatives in accessibility analysis | Low | High | Use reliable libraries and validate results with manual spot checks. |
| Data privacy concerns | Low | High | Ensure all processing is local; do not transmit PDFs or results externally. |
| Limited platform support | Medium | Medium | Clearly document OS requirements; consider future cross-platform development. |
| User error (e.g., incorrect URLs, permissions) | Medium | Low | Provide clear instructions, error messages, and documentation. |

## 9. Success Criteria 

The success of the PDF Auditor project will be measured by the following criteria:

- The application reliably discovers, downloads, and analyzes publicly-linked PDFs from target websites.
- At least 95% of accessible PDFs on tested sites are successfully discovered and processed.
- Accessibility analysis results are accurate and align with manual spot checks (less than 5% false positives/negatives).
- Excel reports are generated correctly and are easy to interpret by stakeholders.
- The GUI is user-friendly and receives positive feedback from at least 80% of pilot users.
- The application completes analysis for a typical website (up to 100 PDFs) within 30 minutes.
- No sensitive user or document data is transmitted externally; all processing is local.
- User documentation enables new users to install and operate the application without external support.
- All major features pass automated and manual QA tests prior to release.
