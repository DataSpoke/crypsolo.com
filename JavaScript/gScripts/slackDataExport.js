/**
This script takes PTO events that were fed from Google Calendar to the MSL Google Sheet and automatically posts them to Slack.
If changes are made to the slack URL changes to this script may be necessary.
Created by mpatterson@iSenpai
**/

function postResponse(fullTitle, fullDesc, fullEvent) {

  var payload = {
    'channel'     : '#i_is_msl',
    'username'    : 'PTO Bot',
    'link_names'  : 1,
    'attachments' :[
       {
          'pretext'   : fullTitle + 'has approved PTO ' + fullDesc,
          'mrkdwn_in' : ['pretext'],
          'color'     : '#D00000',
       }
    ]
  };
  var url     = 'https://hooks.slack.com/services/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';
  var options = {
    'method'  : 'post',
    'payload' : JSON.stringify(payload)
  };
  var response = UrlFetchApp.fetch(url,options);
}