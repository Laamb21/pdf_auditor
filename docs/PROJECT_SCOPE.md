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
| Project Scope Document | A Markdown file that defines the projects purpose, background, objectives, deliverables, milestones, in-scope and out-of-scope featuers, functional and non-functional requirements, assumptions, constraints, risk & mitigation plans, and stakeholders. | TBD | In Progress |
| Technical Requirements Specifications | A detailed spec outlining data inputs/outputs, performance targets, and compliance standards. | TBD | Not Started |
| Web Scraper Module | Component to discover and retrieve all publicly-linked PDFs from a target website. | TBD | Not started |
| Accessibility Analysis Engine | Module to analyze PDFs for PDF/UA and WCAG 2.1 compliance. | TBD | Not started |
| GUI Application | User-friendly desktop interface integrating all modules and workflows. | TBD | Not started |
| Reporting System | Generates Excel reports summarizing compliance results for all analyzed PDFs. | TBD | Not started |
| User Documentation | Guides for installation, usage, troubleshooting, and support. | TBD | Not started |

# 4. Milestones
| Milestone                  | Target Date   | Owner         |
|----------------------------|---------------|---------------|
 | Project Scope & Planning Complete      | 2025-08-05    | Liam Slade      |
 | Technical Requirements Finalized       | 2025-08-12    | Liam Slade      |
 | Web Scraper Module Developed           | 2025-08-19    | Liam Slade      |
 | Accessibility Analysis Engine Complete | 2025-08-26    | Liam Slade      |
 | GUI Prototype Ready                    | 2025-09-02    | Liam Slade      |
 | Reporting System Implemented           | 2025-09-09    | Liam Slade      |
 | User Documentation Drafted             | 2025-09-16    | Liam Slade      |
 | QA & Testing Complete                  | 2025-09-23    | Liam Slade      |
 | Final Release                          | 2025-09-30    | Liam Slade      |

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

## 7.2 Constraints

## 8. Risk & Mitigation
| Risk                        | Probability    | Impact         | Mitigation Plan              |
|-----------------------------|----------------|----------------|------------------------------|
| [Risk 1]                    | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy]        |
| [Risk 2]                    | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy]        |
| [Risk 1]                    | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy]        |
| [Risk 2]                    | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy]        |
| [Risk 1]                    | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy]        |
| [Risk 2]                    | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy]        |

## 9. Stakeholders 
| Stakeholder                 | Role             | Contact Info         |
|-----------------------------|------------------|----------------------|
| [Name / Team]               | [Role]           | [email@example.com]  |
| [Name / Team]               | [Role]           | [email@example.com]  |

