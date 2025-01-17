# Admin

## Members of a team with team maintainer or repository admin permissions can:

- Create a new team and select or change the parent team.
- Delete or rename a team.
- Add or remove organization members from a team, or synchronize a GitHub team's membership with an Identity Provider (IdP) group.
- Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) from team repositories.
- Enable or disable team discussions on the team's page.
- Change the visibility of the team within the organization.
- Manage automatic code review assignment for pull requests, utilizing GitHub's review assignment routing algorithm.
- Schedule reminders.
- Set the team profile picture.

##  Members of an organization with the **owner** permission can perform a wide range of activities at the organization level including:

- Invite users to join the organization, and remove members from the organization.
- Organize users into a team, and grant team maintainer permissions to organization members.
- Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) to organizational repositories.
- Grant repository permission levels to members, and set the base (default) permission level for a given repository.
- Set up organization security.
- Set up billing or assign a billing manager for the organization.
- Extract various types of information about repositories via the use of custom scripts.
- Apply organization-wide changes such as migrations using custom scripts.

## At the enterprise level, members of an enterprise with the owner permissions can:

- Enable security assertion markup language (SAML) single sign-on for their enterprise account, allowing each enterprise member to link their external identity on your IdP to their existing GitHub account.
- Add or remove organizations from the enterprise.
- Set up billing or assign a billing manager for all organizations in the enterprise.
- Set up repository management policies, project board policies, team policies, and other security settings that apply to all the organizations, repositories, and members in the enterprise.
- Extract various types of information about organizations via the use of custom scripts.
- Apply enterprise-wide changes such as migrations via the use of custom scripts.

## Protection rules that can be applied to a branch include:

-Require a pull request before merging.
- Require status checks to pass before merging.
- Require conversation resolution before merging.
- Require signed commits.
- Require linear history.
- Require merge queue.
- Require deployments to succeed before merging.
- Lock the branch by making it read-only.
- Restrict who can push to matching branches.
- Additionally, you can set branch rules that apply to everyone, including administrators. For example, you can allow force pushes to matching branches and allow deletions from users who have push access  

