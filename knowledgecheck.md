# Knowledge check questions

## Which of the following scenarios is a common use case for a version control system? 

1. Deleting earlier versions of a project or file, so you know you are working only with the most current file or data.
2. **Making experimental changes to your project in an isolated branch.**
3. Gathering feature requirements for a large project and communicating them to stakeholders.

## What is another name for a version control system? 

1. Version management software (VMS)
2. Software control management (SCM) system
3. **Software configuration management (SCM) system**

## What’s the difference between Git and GitHub? 

1. **Git lets you work with one or more local branches and push changes to a remote repository. GitHub acts as the remote repository, which is accessed through a website or command-line tools.**
2. Git is a distributed version control system (DVCS) that runs in the cloud. GitHub is an interface layer that provides access to Git technology.
3. Git is used by an individual contributor. GitHub is used by multiple contributors to simplify group development work.

## What Git command gives information about how to use Git? 

1. git init
2. git status
3. **git help**

## What's the difference between GitHub organization accounts and GitHub personal/user accounts? 

1. **Organizational accounts are shared accounts, while personal/user accounts are for individuals.**
2. You pay more for organization accounts versus personal/user accounts.
3. They're exactly the same.
4. Personal/user accounts have more access than organization accounts.

## What's the best reason to decide to upgrade to the GitHub Enterprise product? 

1. Because you want to use GitHub Actions and Codespaces.
2. Because your VP needs to use GitHub Insights.
3. **Because you want to centrally manage users and repositories across multiple organizations.**
4. Because you want to use the team pull request reviewers feature.

##What's the purpose of a team? 
1. A team allows you to manage an organization account.
2. A team allows you to control permission levels for an enterprise.
3. A team allows a single user to sign in using different accounts credentials.
4. **A team is intended to reflect a company or group's structure. It's used to provide cascading access permissions and make it easy to notify all team members via mentions.**

## What's a function you can execute on GitHub Mobile? 

1. Check out branches with pull requests and view CI statuses.
2. Compare changed image.s
3. Add and clone repositories.
4. ** Manage, triage, and clear notifications from github.com.**

## What is GitHub Copilot? 

1. **GitHub Copilot is an AI pair programmer that you can use to get code suggestions.**
2. GitHub Copilot is OpenAI Codex, a new AI system that OpenAI created.
3. GitHub Copilot is a JavaScript public repository and is one of the best-supported languages.
4. GitHub Copilot can write a comment that describes logic, and you can add your suggested code to implement the solution.

## What are the supported IDE extensions for GitHub Copilot? 

1. VS Code and Visual Studio
2. GitHub.com, VS Code, Visual Studio, Neovim, and JetBrains
3. **VS Code, Visual Studio, Neovim, and JetBrains**
   Although GitHub.com is supported, it doesn't need an extension.

## What is the difference between GitHub Copilot Business and GitHub Copilot Enterprise? 

1. GitHub Copilot Enterprise has code completions, whereas GitHub Copilot Business doesn't.
2. GitHub Copilot Enterprise has chat in IDE and mobile, whereas GitHub Copilot Business doesn't.
3. **GitHub Copilot Enterprise has an extra layer of personalization. Organizations use their own codebase to train GitHub Copilot.**
4. GitHub Copilot Enterprise has an extra layer of security, with IP indemnity and enterprise-grade security, safety, and privacy.

## Which directory is the clone placed in after creating a Codespace? 

**/workspaces directory**

/temp directory

~/.bashrc directory

Linux directory

## What's the maximum number of Codespaces that you can create per repository or branch? 

You can only create two Codespaces.

You can create a total of 10 Codespaces.

You can create a total of 30 Codespaces.

**You can create an unlimited number of Codespaces per repository or branch, depending upon available space. When you reach an upper amount of resources, a message displays that an existing Codespace needs to removed/deleted before a new Codespace can be created.**

## What happens when Codespace loses internet connectivity? 

**If the connection to the internet is lost while working in a Codespace, you aren't able to access your Codespace.**

Codespace doesn't require an internet connection. I can access my Codespace regardless if I lose connectivity.

If you lose internet connection while working on your Codespace, your changes aren't saved.

## What defines the beginning of a Codespace's lifecycle? 

**A Codespace's lifecycle begins when you create a Codespace and ends when you delete it.**

A Codespace's lifecycle begins immediately when GitHub is opened and ends when the software is closed.

A Codespace's lifecycle begins when a repository is created and ends when you delete it.

## What Project descriptor automatically saves when you change it? 

**Project name**

Project description

Project README

## What does an iteration field help you do in Projects? 

Allows you to keep track of the various changes made to an issue or pull request.

Allows you to reverse the changes you made to your Project.

**Allows you to create sequential phases of your project and group issues and pull requests based on the phase.**

***An iteration field helps you and your team organize your Project into different phases. The value of the field allows you to prioritize what comes first. Setting priorities allows you to implement timelines to keep you on track and accomplish your goals.***

## What field can you use in order to make a Priority grouping like High, Medium, and Low in your Project? 

Date

**Single select**
***The Single select field allows you to create multiple groups like Priority grouping in order to help you organize and prioritize your Project.***

Iteration field

## What is the easiest way to add automation to your Project? 

GraphQL API

**Built-in Automation**
***Built-in automation built within Projects allows you a simple way to automate your Project.***

GitHub Actions

## What is the name of the section where you can change the visibility of your Project, close your Project, or delete your Project? 

Red zone

Visibility and Access

**Danger zone**

## Which of the following Markdown snippets produces the text Hello, world! in bold italics? 

\*Hello, \*world\*!\*

\*\*Hello, \*world\*!\*\*

\*\*\*Hello, world!\*\*\*

***Hello, world!***
**bold** is produced with two asterix on either side of the word and *italics* with one on each side. You can also use underscores (_) instead of asterisks if you prefer.

\#\#\# Hello, world!

## How do you print certain characters, like asterisks (*) and underscores (_), literally on your output? 

Use three in a row, like *** or ___.

**Escape them with a backslash, like \* or \_.**
You can also escape other reserved characters, including { and #, using backslashes.

Unfortunately, this isn't supported at this time.

## Suppose there's an HTML snippet that you want to include on your GitHub Pages web site, but Markdown doesn't offer a way to render it. What should you do? 

**Just add the HTML inline.**
Markdown isn't a complete replacement for HTML. You might need to add HTML to get the final results you're looking for.

Cut the content. If it's not supported in Markdown, then it's probably not worth including.

Open an issue that requests Markdown support for your specialized scenario.

## You want to grant a user the permissions required to add and remove organization members to and from a team. Which permission would you need to grant that user? 

The admin permission on a repository

The maintain permission on a repository

Organization billing manager

**Team maintainer**
As a team maintainer, the user can add and remove organization members to and from a team.

## As an organization owner, you want to ensure that everyone who is signed in to your corporate network can access the GitHub website without requiring a second sign-in. Which technology would you enable to accomplish this? 

**Single sign-on**
Single sign-on is the right technology to allow network users to access the GitHub website without extra sign-ins.

Two-factor authentication

Personal Access Tokens

SSH keys

## What's the appropriate repository permission level for contributors who need to actively push changes to your repository? 

Admin

**Write**
The write permission is the appropriate permission level.

Triage

Maintain

## What is not a good reason to create a pull request? 

You would like to receive feedback on prospective changes before merging your feature branch into main.

You want to merge your bug fix branch into main, but don't have permission.

**Your branch can't be merged into main due to upstream changes made since you created it. Creating a pull request lets the other contributor know they need to pull their changes out so you can put yours in.**
Pull requests don't work this way. Also, the etiquette is for you to be sure your branch can be cleanly merged into the base before creating a pull request.


## How can you ensure that pull requests for a given area of the repository, aren't merged unless certain users or teams approve? 

Clearly explain the pull request policy in CONTRIBUTING.md.

**Use a CODEOWNERS file and enable required reviews.**
A CODEOWNERS file enables you to assign users or teams as required reviewers using the same syntax as .gitignore files.


Add a table that maps directory paths to required users in SECURITY.md.

## You're requested to review a pull request. As you read through it, you notice several minor coding errors and typos. How should you handle the review? 

**Start a review and fix obvious typos inline. Add comments in places that require further discussion or offer educational value. Complete the review with changes requested.**
Contributors always appreciate when reviewers show an interest in getting their code merged.

Leave single comments for each issue you come across, but don't change the code. For typos, include the correct spelling of the word as a reference. Approve the pull request if you trust the author to implement your suggestions.

Reject the pull request. We can't risk any bugs accidentally being merged into an important branch.

## How does GitHub's top-level search bar differ from the search options available on repository tabs? 

Other than being located in different parts of the user interface, they are otherwise the same.

They support different filter syntax options.

**The top-level search bar supports searching everything across all of GitHub, whereas the repository tab searches are scoped to cover specific types in the current repository.**
The top-level search allows the most flexibility, whereas the scoped tab searches provide popular filter dropdowns for easier refinement.

## What does git blame do? 

It creates a bug assigned to the last person who committed changes to the specified file.

**It displays the commit history of the file.**
Despite the accusatory name, git blame is just a command to display commit history.

It reverts the effects of a git praise command.

## Suppose a bug issue is reported on your project, and you know which pull request introduced the problem. Which of the following options is not a cross-linking best practice? 

**Do not create cross-links when the root cause of the issue is already known.**
It's a good practice to always add cross-links in case you or someone else needs the context later on.

Add a comment to the bug report that includes the pull request's author by using an @mention.

Add a comment to the bug report that links the pull request to it using the #ID syntax.

## How does GitHub Copilot work? 

**GitHub Copilot uses prompts and natural language text that you type to provide coding suggestions.**
GitHub Copilot is trained on billions of lines of code. It turns natural language prompts into coding suggestions across dozens of languages.

GitHub Copilot uses lights, that you type, and it provides suggestions based on what you type.

GitHub Copilot uses radio language, that you type, and it provides suggestions based on what you type.

## What are some GitHub Copilot Free features? 

It's a free unrestrticted AI tool that works independent of code editors.

**It provides several suggestions and chats per month directly in your IDE and on github.com.**
 It also supports multi-file editing and and switching models!

An option to enable slower responses, preservering your Copilot Pro quota.

## How can you accept GitHub Copilot's suggestions? 

**Press the Tab key.**
Copilot offers you a suggestion, which appears as grey code if you use black as your text color. To accept the suggestion, you need to press the Tab key.

Press the F1 key.

Press the F4 key.

## Identify which statement is valid and select the correct answer: 

A prompt, which is our output, is a collection of songs that tells our copilot what to generate.

**A prompt, which is our input, is a collection of instructions or guidelines that tell our copilot what to generate.**
A prompt is crucial in eliciting specific responses from Copilot. The prompt might be a comment that steers Copilot to generate code on your behalf or writing code that Copilot autocompletes.

A prompt, which is our document, is a collection of laptops that tells our Copilot what to generate.

## What does the quality of the output from GitHub Copilot depend on? 

Your code editor.

How well your extensions were installed.

**How well you crafted your prompt.**
Designing an effective prompt is, therefore, crucial in ensuring we achieve our desired outcomes. You need to detail your prompt as much as possible.

## GitHub Action workflows are triggered by events. Which of these are valid events that GitHub Actions support? (Choose two.)

A new member has been added to the repository

A change is made to the repository settings

A new vulnerability has been detected in a dependency

**A commit is pushed to a branch**

**A pull request is opened**

[💡Hint](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#about-events-that-trigger-workflows)

## What are the possible statuses for a pull request review? (Choose three.)

**Approve**

Close

**Comment**

**Request Changes**

Deny

Applaud

[💡Hint](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews#about-pull-request-reviews)

## What are the different available options for adding issues and pull requests to a GitHub Project board?

**Individually, automatically, or in bulk.**

Only individually or in bulk

Only manually, one at a time.

Only automatically using project workflows

[💡Hint](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#adding-issues-and-pull-requests-to-a-project)

## What feature is unique to GitHub Desktop compared to github.com?

View repository insights

**Visualize branch histories in a graphical interface**

Create new repositories

Clone repositories to local machine

[💡Hint](https://docs.github.com/en/desktop/making-changes-in-a-branch/viewing-the-branch-history-in-github-desktop)
[💡💡Hint2](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-the-activity-view-to-see-changes-to-a-repository)

GitHub Desktop provides a graphical interface for visualizing branch histories, which is unique compared to the website

## What is a repository in GitHub?

A repository in GitHub is a chat room where developers can discuss code-related issues.

**It's a place where you can store your code, your files, and each file's revision history.**

It's a place where you can store your Docker images or NPM packages.

It's a visual code editor that allows you to edit your source code in the browser.

[💡Hint](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)

## Which of the GitHub features best serves as a simple way to share small code snippets with others?

Issues

Projects

Wikis

**Gists**

[💡Hint](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)

## What is a GitHub Codespace deep link?

It's a link to the most recent GitHub Codespace that was created for the repository

It's a link between the GitHub Codespace and the repository which keeps the Codespace in sync with the changes in the repository

It's a link to the most recent GitHub Codespace that you have used in any repository

**It's a link that points to a specific GitHub.com Page that allows you to create a new GitHub Codespace and select specific configuration**

[💡Hint](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#configuring-more-options)







