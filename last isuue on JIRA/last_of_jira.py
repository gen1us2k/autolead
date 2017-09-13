import sys
from optparse import OptionParser

from jira import JIRA


def last_issue_by_user(username, password, assignee):
    jira = JIRA(basic_auth=(username, password), options={'server': 'https://pm.maddevs.co/'})
    var = "assignee = '{}' order by created desc".format(assignee)
    last_issue = jira.search_issues(var)[0]
    issue = jira.issue(last_issue)
    name = issue.fields.issuetype.name
    assignee = issue.fields.assignee.displayName
    print(name, 'by ', assignee)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="username", help="Username from JIRA")
    parser.add_option("-p", "--password", dest="password", help="Password from JIRA")
    parser.add_option("-a", "--assignee", dest="assignee", help="Assignee in JIRA")

    (options, args) = parser.parse_args()
    if not options.username or not options.assignee:
        parser.print_help()
        sys.exit(0)

    print(last_issue_by_user(options.username, options.password, options.assignee))
