/**
This script takes PTO events that were fed from Babmoo to Google Calendar and automatically appends it to the MSL Google Sheet.
If changes are made to the Bamboo feed URL, to the location of the calendar, or to the location of the MSL spreadsheet in Google Drive, changes to this script may be necessary.
Created by mpatterson@iSenpai
**/

function getCalUpdates() {
  
  //Calender ID obtained from settings of Google Calendar for PTO
  var calendar  = CalendarApp.getCalendarById('INSERT_CALENDAR_ID');
  var sheet     = SpreadsheetApp.openById('INSERT_SHEET_ID');
  var calEvents = calendar.getEventsForDay(new Date());
  var nextRow   = getNextRow(sheet) + 1;
  var specificSheet = sheet.getSheets()[0];
  
  //Loop variables
  var l = calEvents.length;
  var i;
  
  for (i=0;i<l;i++) {
    
    specificSheet.insertRowAfter(1);
    
    //Grabs title of calendar entry and performs string formatting
    var eventTitle  = String([[calEvents[i].getTitle()]]);
    var eventTitleF = eventTitle.indexOf('(');
    var fullTitle   = eventTitle.slice(0, eventTitleF);
    
    //Grabs description of calendar entry and performs string formatting
    var eventDesc   = String([[calEvents[i].getDescription()]]);
    var eventDescF  = eventDesc.indexOf('(');
    var fullDesc    = eventDesc.slice(eventDescF).toUpperCase(); 
    
    //Start and end times of event; don't need because start/end time are included in the event description
    //var eventStart  = [[calEvents[i].getStartTime()]];
    //var eventEnd    = [[calEvents[i].getEndTime()]];
    
    var fullEvent = String(fullTitle + 'has approved PTO ' + fullDesc);
    
    sheet.getRangeByName('personnel').getCell(nextRow, 1).setValue('PTO Bot');
    sheet.getRangeByName('entry').getCell(nextRow, 1).setValue(fullEvent);
    sheet.getRangeByName('timestamp_date').getCell(nextRow, 1).setValue(new Date());
    sheet.getRangeByName('timestamp_time').getCell(nextRow, 1).setValue(new Date());
    
    postResponse(fullTitle, fullDesc, fullEvent);

  }
}

//Un-comment for use in production  
/**function getNextRow(sheet) {
  var timestamp = sheet.getRangeByName("pivot").getValues();
  for (i in timestamp) {
    if(timestamp[i][0] == "") {
      return Number(i);
      break;
    }
  }
}**/
