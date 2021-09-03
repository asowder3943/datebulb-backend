# What is Datebulb?

Datebulb is a cross platform application that helps users and their romantic partners make decisions on date night.

It also offers journaling features that serve as a digital scrapbook for couples.

# Our Mission and Purpose

We believe that datebulb will induce meaningful interactions and strengthen relationships.

We hope that the application's friendly, colorful interface and positive messaging will remind our users to cherish their existing memories and create new ones.

# The Team

**Needs Implementation**

# Backend Technologies

The backend of the datebulb application consists of a restful django API. The current build targets a MongoDB noSQL database.

# Current State of the Project

The First version of the datbulb restful API is still being built. A more detailed view of the projects status can be viewed at the prototyping project board:

https://github.com/asowder3943/datebulb-backend/projects/1

# Contribution Guide

Datebulb, in addition to being user facing application, is indeed a resume project.

In order to best display the capabilities of the team the following conventions should be taken when contributing to the application.

## Priority of Action

Ideally each contribution session should consist of 5 parts:

**_Collaboration - Review - Commits - Claims - Plans_**

1. **Catch Up with The Team** - Zoom Calls are every Mon-Wed-Fri from ~10:30AM - 3:00PM. For specific times consult the DateBulb GroupMe chat (Invite Only)

```
git pull
```

2. **Code Review and Merges** - By policy no pull requests can be merged by the creator of that pull request. The number one priority of contributors is reviewing existing code. This way, no pull requests go stale and contributors are prompted to stay up to date with the latest changes. Review the difs of the latest code changes and ask questions to the requestor if there is confusion about any changes in the code.

https://github.com/asowder3943/datebulb-backend/pulls

3. **Commiting changes and creating pull requests** - Issues are assigned and addressed one at a time. If you assign yourself an issue to address, try to complete those commits and submit pull requests ASAP. Issues should be specific enough to be solved in < 1 hour of coding.

```
git push origin issue_x
```

4. **Claim Existing Open Issues** - If a new issue has been opened, but is unassigned, attempt to resolve these issues before opening new ones.

```
git branch issue_x
git checkout issue_x
git add -A
git commit -m "<useful commit message>"
```

5. **Create New Issues** - Using the current active Project board, convert tasks to new issues so they can be addressed in the next coding sesh. If there are no open taks on the project board, collaborate with the team to brainstorm the next set of project tasks.

![convert to issue](https://raw.githubusercontent.com/asowder3943/datebulb-backend/main/img/convert_to_issue.png?raw=true)

## Conventions

1. No pull requests should be made without first creating an issue to document the original intent of the changes
2. Branch Names should be named after the issue they are addressing.
3. All issues should be able to be resolved in one coding session. Unless they are created to document major bugs. If a issues is created that is too large to be completed in one pull request, then sub issues should be created that reference that larger issue in the description.
