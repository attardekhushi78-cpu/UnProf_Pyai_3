<a id="top"></a>

# 📁 ScholarOps Directory — Day 3 Submission

### An exceptionally stable, persistent Contact Management System featuring automated diagnostic tracking logs and granular constraint-validation pipelines.

<p align="center">
  A robust data sandbox demonstrating system crash protection frameworks, customized trigger boundaries, and native Python logging pipelines.
  <br />
  <a href="https://drive.google.com/file/d/1-csO9N4skGZXOa_ba3EutEKbTdRDdR9Z/view?usp=sharing"><strong>Explore App Demo »</strong></a>
  <br />
  <br />
  <a href="https://github.com/attardekhushi78-cpu/unprof">Explore Codebase</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/unprof/issues">Report Bug</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/unprof/issues">Request Feature</a>
</p>

## 📖 Table of Contents

* [Features](#-features)
* [Documentation Index](#-documentation-index)
* [Getting Started & Installation](#-getting-started--installation)
* [Usage State Flow](#-usage-state-flow)
* [Roadmap](#-roadmap)
* [Contributing](#-contributing)


---

## Features
ScholarOps advances data processing mechanics by building highly secure error wrappers around runtime tasks.
🛡️ Defensive Try-Except-Else-Finally Workflows: Manages processing cycles safely by splitting application triggers from memory-commit states.
🪵 Real-Time Automated Diagnostic Logging: Writes timestamped application events, structural errors, and operational footprints straight to a dedicated system file.
🛑 Custom Sub-Class Exceptions: Implements targeted error checking (DuplicateContactError and InvalidContactInputError) to isolate execution exceptions cleanly.🩹 Graceful Corruption Self-Healing: Monitors file initialization sequences to handle missing or broken data lines safely without crashing the main terminal runtime loop.

## Documentation Index
To keep the repository documentation highly maintainable, core implementation designs are mapped out below:
The application implements a multi-tiered validation approach inside its try-except-else-finally matrix:The Try Matrix: Validates raw text parameters for blank variables or matching lowercase names before processing.
The Catch Barriers: Funnels explicit validation triggers into dedicated custom exception handlers to filter errors granularly.
The Else Gate: Guarantees that data-serialization write operations (json.dump) run only if input validations pass completely.
The Finally Boundary: Executes final system cleanup logs and terminal notices regardless of whether exceptions were raised.System events are systematically structured within app_activity.
log utilizing the following configuration flags:INFO: Captures successful framework startups, graceful exit calls, verified search outputs, and successful profile commits.
        WARNING: Registers input validation rejections, duplicate profile registration attempts, and initial missing-file parameters.
        CRITICAL / ERROR: Tracks data formatting leaks, file corruption alerts (json.JSONDecodeError), and failing hardware stream pipelines.
        
        
## Getting Started & Installation
To boot up the application local workspace environment and view active logs, run these terminal steps:PrerequisitesPython 3.8 or higher installed. 
No external package management downloads (pip install) are required as the software runs purely on native built-in libraries.
System InitializationBash# 1. Clone the assignment workspace repository from GitHub
git clone [https://github.com/github_username/unprof.git](https://github.com/github_username/unprof.git) && cd unprof

# 2. Confirm your local Git remote configurations
git remote -v

# 3. Boot up the application environment
python contact_manager.py
💻 Usage State FlowPhaseInput ActionExpected Validation ProcessingLog File Outcome (app_activity.log)1Add Valid EntryEnters complete alpha-numeric name keys and phone digit strings under Option 1.Generates an INFO flag tracking successful serialization and storage sync.2Test Blank RejectionAttempts to press Enter on mandatory fields without input parameters.Raises InvalidContactInputError and drops execution before disk commit.3Test Duplicate BlockingInputs a pre-existing contact profile name using different letter casing.Raises case-insensitive DuplicateContactError and logs a system WARNING.4Check Active LogsAccesses Option 4 to exit the script container gracefully.Finalizes and closes the active file streaming append pipeline cleanly.Code Showcase: Custom Error & Else Logic WrapperPythontry:
    if not name or not phone:
        raise InvalidContactInputError("Name and Phone Number are strictly mandatory fields.")
    
    for contact in contacts_list:
        if contact["name"].lower() == name.lower():
            raise DuplicateContactError(f"A profile record under the name '{name}' already exists.")

except DuplicateContactError as error_msg:
    print(f"❌ Input Rejection: {error_msg}")
    logging.warning(f"Registration Replaced Attempt: Duplicate check hit for target name '{name}'.")
    return

 
## Roadmap[x] 
Phase 1 Day 2: Implement persistent data models with local JSON file processing channels.[x] Phase 1 Day 3: Build custom try-except structural error tracking boundaries.[x] 
Phase 1 Day 3: Integrate native logging stream diagnostics file generators.[ ] 

Phase 2: Add single-entry removal and dynamic data updating options.[ ] Phase 2: Integrate multi-format conversion pipelines (JSON to CSV/Text exporting engines).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any modifications or upgrades to optimize these software structures are highly valued.If you have a structural suggestion that would make this model better, please fork the repository workspace and open a clean pull request. You can also simply open an issue ticket flagged with the "enhancement" metadata tag.Fork the Project WorkspaceCreate your Feature Branch (git checkout -b feature/AmazingFeature)Commit your configuration updates safely (git commit -m 'Add some AmazingFeature')Push code updates directly to your tracking origin (git push origin feature/AmazingFeature)Open a professional Pull Request
