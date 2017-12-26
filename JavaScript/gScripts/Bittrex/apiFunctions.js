function APIFunctions() {
    
    //Used to get the open and available trading markets at Bittrex along with other meta data
    var public_getMarkets =        JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getmarkets').getContentText());

    //Used to get all supported currencies at Bittrex along with other meta data
    var public_getCurrencies =     JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getcurrencies').getContentText());

    //Used to get the current tick values for a market
    //Params: market (ex: BTC-LTC)
    var public_getTicker =         JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getticker').getContentText());

    //Used to get the last 24 hour summary of all active exchanges
    var public_getSummaries =      JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getmarketsummaries').getContentText());

    //Used to get the last 24 hour summary of a single active exchange
    //Params: market (ex: BTC-LTC)
    //var public_getSummary =      JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getmarketsummary?market=).getContentText());

    //Used to get retrieve the orderbook for a given market
    //Params: market (ex: BTC-LTC), type (buy, sell, both)
    //var public_getOrderBook =    JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getorderbook?market=&type=').getContentText());

    //Used to retrieve the latest trades that have occured for a specific market
    //Params: market (ex: BTC-LTC)
    //var public_getMarketHist =   JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/public/getmarkethistory?market=').getContentText());

    //Used to place a buy order in a specific market. Use buylimit to place limit orders. 
    //Make sure you have the proper permissions set on your API keys for this call to work
    //Params: market (ex:BTC-LTC), quantity, rate
    //var market_buyLimit =        https://bittrex.com/api/v1.1/market/buylimit?apikey=API_KEY&market=BTC-LTC&quantity=1.2&rate=1.3
    //TO DO: Parameter input formatting

    //Used to place an sell order in a specific market. Use selllimit to place limit orders. 
    //Make sure you have the proper permissions set on your API keys for this call to work
    //Params: market (ex:BTC-LTC), quantity, rate
    var market_sellLimit =         JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/market/selllimit?apikey='+readKey+'&market=BTC-LTC&quantity=1.2&rate=1.3').getContentText());
    //TO DO: Parameter input formatting

    //Used to cancel a buy or sell order
    //Params: uuid (uuid of buy/sell order)
    var market_cancel =            JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/market/cancel?apikey='+readKey+'&uuid=ORDER_UUID').getContentText());
    //TO DO: Parameter input formatting

    //Get all orders that you currently have opened. A specific market can be requested
    //Params: market (ex: BTC-LTC)
    var market_getOpenOrd =        JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/market/getopenorders?apikey='+readKey+'&market=BTC-LTC').getContentText());

    //Used to retrieve all balances from your account
    var account_getBals =          JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getbalances?apikey='+readKey).getContentText());

    //Used to retrieve the balance from your account for a specific currency
    var account_getBal =           JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getbalance?apikey='+readKey+'&currency=').getContentText());

    //Used to retrieve or generate an address for a specific currency. If one does not exist, the call will fail and return ADDRESS_GENERATING until one is available
    //Params: currency (ex: BTC, ETH)
    var account_getAddress =       JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getdepositaddress?apikey='+readKey+'&currency=').getContentText());

    //Used to withdraw funds from your account. note: please account for txfee
    //Params: currency, quantity, address, paymentid (optional)
    var account_withdraw =         JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/withdraw?apikey=API_KEY&currency=EAC&quantity=20.40&address=EAC_ADDRESS').getContentText());

    //Used to retrieve a single order by uuid
    //Params: uuid (uuid of buy/sell order)
    var account_getOrder =         JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getorder&uuid=').getContentText());

    //Used to retrieve your order history
    //Params: market (optional) (ex: BTC-LTC)
    var account_getOrderHist =     JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getorderhistory').getContentText());

    //Used to retrieve your withdrawal history
    //Params: currency (ex: BTC, ETH)
    var account_getWithdHist =     JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getwithdrawalhistory?currency=').getContentText());

    //Used to retrieve your deposit history
    //Params: currency (ex: BTC, ETH)
    var account_getDepHist =       JSON.parse(UrlFetchApp.fetch('https://bittrex.com/api/v1.1/account/getwithdrawalhistory?currency=BTC').getContentText());

}
