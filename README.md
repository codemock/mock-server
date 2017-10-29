mock-server is server which spikes server according to data provided.
all the data is first provided in output.json
future roadplan:
    provide an api to dynamically add output.json
    provide an api to clear earlier mock-data


add 
{
    # url 
    "/ram":{
        # specifiys post or get
        "GET":[{
            # providing following response according to query string
            "query_string":{"a":"10"},
            "response":"asdf"
        },
        {
            "query_string":{"a":"11"},
            "response": "this is bad"
        }
        
    ],
        "POST": [{
            "query_string":{},
            "post_data":"",
            "response":""
        }]
    }
}