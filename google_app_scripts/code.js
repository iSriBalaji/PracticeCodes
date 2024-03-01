function matchAndCopyRecords() {
  var sheet1 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Leads");
  var sheet2 = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("OneBill");
  var sheet3 = SpreadsheetApp.openById("1B4w7QpesIj3BwUpGmyjImJm3s0kTQ2uy_DIi40vhMKQ");

  var sheet1Data = sheet1.getDataRange().getValues();
  var lastSheet2Record = sheet2.getDataRange().getValues().pop();

  var lastSheet2Email = lastSheet2Record[4].trim().toLowerCase();
  var lastSheet2PhoneNumber = trimPhoneNumber(String(lastSheet2Record[5]));
  
  for (var i = 0; i < sheet1Data.length; i++) {
    var sheet1Email = sheet1Data[i][2].trim().toLowerCase(); // Access email in sheet1
    var sheet1PhoneNumber = trimPhoneNumber(String(sheet1Data[i][4])); // Access phone number in sheet1

    if (sheet1Email === lastSheet2Email || sheet1PhoneNumber === lastSheet2PhoneNumber) {
      Logger.log("Match found in sheet1: " + sheet1Data[i][15]);
      var rowData = [].concat(lastSheet2Record, sheet1Data[i][15]);
      // sheet3.appendRow(lastSheet2Record + sheet1Data[i][15]);
      sheet3.appendRow(rowData);
    }
  }
}


function trimPhoneNumber(phoneNumber) {
  var regex = /^\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})$|^([+]\d{1,2}[-\s]?)\(?(\d{3})\)?[-. ]?(\d{3})[-. ]?(\d{4})$/;
  var match = phoneNumber.match(regex);

  return match ? match[1] + '-' + match[2] + '-' + match[3] : '';
}
