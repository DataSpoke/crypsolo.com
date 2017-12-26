function getCoinUpdates() {
  
  //Replace sheet IDs as needed; obtained from URL of sheet
  var sheet = SpreadsheetApp.openById('INSERTSHEETID');
  var specificSheet = sheet.getSheets()[0];
  
  //Etherscan.io account balance retrieval; Replace address and API keys as needed; Etherscan API keys only necessary if running more than 5 queries per second
  var getETHBal = JSON.parse(UrlFetchApp.fetch('https://api.etherscan.io/api?module=account&action=balance&address=INSERTWALLETADDRESS&tag=latest&apikey=INSERTAPIKEY').getContentText());
  var getGNTBal = JSON.parse(UrlFetchApp.fetch('https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xa74476443119A942dE498590Fe1f2454d7D4aC0d&address=INSERTWALLETADDRESS&tag=latest&apikey=INSERTAPIKEY').getContentText());
  var getBATBal = JSON.parse(UrlFetchApp.fetch('https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x0d8775f648430679a709e98d2b0cb6250d2887ef&address=INSERTWALLETADDRESS&tag=latest&apikey=INSERTAPIKEY').getContentText());
  
  //Coinmarketcap.com data retrieval
  var getETH = JSON.parse(UrlFetchApp.fetch('https://api.coinmarketcap.com/v1/ticker/ethereum/').getContentText());
  var getSC  = JSON.parse(UrlFetchApp.fetch('https://api.coinmarketcap.com/v1/ticker/siacoin/').getContentText());
  var getBAT = JSON.parse(UrlFetchApp.fetch('https://api.coinmarketcap.com/v1/ticker/basic-attention-token/').getContentText());
  var getGNT = JSON.parse(UrlFetchApp.fetch('https://api.coinmarketcap.com/v1/ticker/golem-network-tokens/').getContentText());
  
  //Coin worth data
  sheet.getRangeByName('ETHWorth').setValue(getETH[0].price_usd);
  sheet.getRangeByName('SCWorth').setValue(getSC[0].price_usd);
  sheet.getRangeByName('BATWorth').setValue(getBAT[0].price_usd);
  sheet.getRangeByName('GNTWorth').setValue(getGNT[0].price_usd);
  
  //1 Hour change data
  sheet.getRangeByName('ETHPerc1Hr').setValue(getETH[0].percent_change_1h);
  sheet.getRangeByName('SCPerc1Hr').setValue(getSC[0].percent_change_1h);
  sheet.getRangeByName('BATPerc1Hr').setValue(getBAT[0].percent_change_1h);
  sheet.getRangeByName('GNTPerc1Hr').setValue(getGNT[0].percent_change_1h);
  
  //24 Hour change data
  sheet.getRangeByName('ETHPerc24Hr').setValue(getETH[0].percent_change_24h);
  sheet.getRangeByName('SCPerc24Hr').setValue(getSC[0].percent_change_24h);
  sheet.getRangeByName('BATPerc24Hr').setValue(getBAT[0].percent_change_24h);
  sheet.getRangeByName('GNTPerc24Hr').setValue(getGNT[0].percent_change_24h);
  
  //7 Day change data
  sheet.getRangeByName('ETHPerc7Day').setValue(getETH[0].percent_change_7d);
  sheet.getRangeByName('SCPerc7Day').setValue(getSC[0].percent_change_7d);
  sheet.getRangeByName('BATPerc7Day').setValue(getBAT[0].percent_change_7d);
  sheet.getRangeByName('GNTPerc7Day').setValue(getGNT[0].percent_change_7d);
  
  //Balance Data
  var ETHBal = getETHBal.result
  sheet.getRangeByName('ETHBal').setValue(ETHBal / 1000000000000000000);
  var GNTBal = getGNTBal.result
  sheet.getRangeByName('GNTBal').setValue(GNTBal / 1000000000000000000);
  var BATBal = getBATBal.result
  sheet.getRangeByName('BATBal').setValue(BATBal / 1000000000000000000);
  
  //Date data
  var currentDate = new Date();
  sheet.getRangeByName('curDate').setValue(currentDate);
  
  //Logging for test purposes
  //Logger.log(GNTBal);
  //Logger.log(getETH[0].price_usd);

}
