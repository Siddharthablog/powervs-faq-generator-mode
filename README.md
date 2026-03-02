# 📋 PowerVS FAQ Generator Mode for BOB

Automatically generate FAQ entries from PowerVS documentation using BOB (Business Operations Bot). This mode follows IBM Cloud Docs FAQ patterns and structure.

## 🚀 Quick Start

1. **Copy the mode configuration** to your BOB setup
2. **Place all files** from `.bob/` directory into your BOB rules folder
3. **Restart BOB** to load the new custom mode
4. **Use the mode** by selecting "PowerVS FAQ Auto-Generator" when creating documentation

## 📁 Repository Structure

```
powervs-faq-generator-mode/
├── custom_modes.yaml              # Mode registration and definition
├── .bob/
│   ├── 1_faq_workflow.xml         # FAQ extraction workflow steps
│   ├── 2_faq_patterns.xml         # PowerVS FAQ patterns & templates
│   └── (additional rules files)   # Extended rules as needed
└── README.md                      # This file
```

## 🎯 Features

### Automatic FAQ Generation
- **3-5 FAQ questions** extracted from a single .md documentation file
- **Structured Q&A pairs** in PowerVS FAQ format
- **Cross-reference links** connecting FAQs to source documentation
- **Proper metadata** (anchors, tags, deployment indicators)

### IBM Cloud Docs Compliance
- Uses `{{site.data.keyword.*}}` variables
- Follows PowerVS faq.md structure and patterns
- Deployment tagging: `[tag-blue]` for public cloud, `[tag-red]` for private cloud
- Anchor naming conventions (kebab-case)
- Support tags: `{: faq} {: support}`

### FAQ Patterns Included
1. **Conceptual FAQs** - "What is..." questions
2. **Comparison FAQs** - "What's the difference..." questions  
3. **Procedure FAQs** - "How do I..." questions
4. **Capability FAQs** - "Can I..." yes/no questions
5. **Technical Specification FAQs** - "What are the specs..." questions

## 📚 How It Works

### Input
You provide a PowerVS documentation .md file (e.g., network configuration guide, troubleshooting doc)

### Processing
BOB:
1. Analyzes content for FAQ-worthy questions
2. Matches patterns against PowerVS FAQ templates
3. Generates markdown Q&A entries
4. Creates cross-reference links
5. Outputs 3 sections: raw FAQ entries, line numbers, cross-reference mapping

### Output
```markdown
## Can I set VM affinity rules for high availability?
{: #can-i-set-affinity-rules}
{: faq}

[{{site.data.keyword.off-prem}}]{: tag-blue}

Yes. You can apply affinity and anti-affinity policies to VMs and volumes...

For more information, see [VM pinning documentation](url).
```

## 🛠️ Installation

### For IBM Enterprise BOB Users

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/Siddharthablog/powervs-faq-generator-mode.git
   ```

2. **Copy files to your BOB setup**
   ```bash
   cp custom_modes.yaml /path/to/bob/.bob/
   cp .bob/* /path/to/bob/.bob/rules-powervs-faq-generator/
   ```

3. **Update custom_modes.yaml** in your main BOB configuration to register this mode

4. **Restart BOB**

### For BOB Integration

Add to your `custom_modes.yaml`:
```yaml
customModes:
  - slug: powervs-faq-generator
    name: 📋 PowerVS FAQ Auto-Generator
    roleDefinition: |
      [See custom_modes.yaml for full definition]
    groups:
      - read
      - edit
      - command
```

## 📖 Usage Examples

### Example 1: From a Networking Guide
**Input:** `network-planning.md` (documentation on networking setup)
**Output:** 4 FAQ entries:
- "What networking setup is required?"
- "Can I configure custom subnets?"
- "How do I set up VPN connectivity?"
- "What are the network bandwidth limitations?"

### Example 2: From Troubleshooting Doc
**Input:** `troubleshoot-aix.md` (AIX-specific troubleshooting)
**Output:** 3-4 FAQ entries covering common issues and solutions

## 🔍 Pattern Examples

### Simple "What is" FAQ
```markdown
## What is {{site.data.keyword.powerSysFull}}?
{: #what-is-powervs}
{: faq}

{{site.data.keyword.powerSys_notm}} is an IBM Power server offering that allows you to deploy virtual servers...
```

### Deployment-Specific FAQ
```markdown
## What are the deployment options?
{: #deployment-options}
{: faq}

[{{site.data.keyword.off-prem}}]{: tag-blue}
Public cloud option deployed in IBM data centers.

[{{site.data.keyword.on-prem}}]{: tag-red}
Private cloud option deployed in your data center.
```

## ⚙️ Configuration Files

### `custom_modes.yaml`
Defines the PowerVS FAQ Generator mode with:
- Mode slug, name, and emoji
- Role definition (AI system prompt)
- Usage guidelines
- Access groups (read, edit, command)

### `.bob/1_faq_workflow.xml`
Stepwise workflow for FAQ extraction:
- Content analysis (identify questions)
- Pattern matching (against PowerVS templates)
- Markdown generation
- Cross-reference creation
- Output formatting

### `.bob/2_faq_patterns.xml`
PowerVS-specific FAQ patterns:
- 5 FAQ pattern templates
- Naming conventions (kebab-case anchors)
- Deployment tagging rules
- IBM Cloud Docs variable requirements

## 🎓 Best Practices

1. **Use with concept/procedure docs** - FAQs work best when extracted from structured documentation
2. **Review generated FAQs** - AI-generated content should be reviewed for accuracy before publishing
3. **Maintain consistency** - Follow existing PowerVS FAQ naming and tagging conventions
4. **Cross-reference thoroughly** - Link FAQs back to full documentation
5. **Tag appropriately** - Use deployment tags correctly (public/private/both)

## 📊 Time Savings

| Task | Manual | BOB-Assisted | Savings |
|------|--------|--------------|----------|
| Read & analyze .md | 5 min | Auto | 5 min |
| Extract key questions | 10 min | Auto | 10 min |
| Write FAQ answers | 20 min | 5 min | 15 min |
| Format FAQ entries | 5 min | Auto | 5 min |
| Create cross-references | 10 min | Auto | 10 min |
| **Total per FAQ** | **50 min** | **5 min** | **90%** |

## 🤝 Contributing

To improve this mode:
1. Fork the repository
2. Add new patterns or rules to `.bob/` files
3. Test with PowerVS documentation
4. Submit a pull request

## 📝 License

MIT License - Feel free to use and modify for your documentation needs

## 👤 Author

**Siddhartha** - Information Developer & AI Documentation Specialist
- Email: mani.siddhartha@gmail.com
- GitHub: [@Siddharthablog](https://github.com/Siddharthablog)
- Interests: AI documentation, technical writing automation, IBM Cloud services

## 🔗 Related Resources

- [PowerVS Documentation](https://cloud.ibm.com/docs/power-iaas)
- [IBM Cloud Docs Style Guide](https://cloud.ibm.com/docs/writing)
- [BOB Documentation](https://github.ibm.com/ibmcloud/content-kit)
- [PowerVS FAQ Example](https://github.ibm.com/cloud-docs/power-iaas/blob/source/faq.md)

## ✨ Acknowledgments

This mode is built following the patterns from:
- PowerVS official documentation repository
- IBM Cloud Docs writing standards
- BOB content-kit rules structure

---

**Last Updated:** March 2, 2026
**Version:** 1.0.0
