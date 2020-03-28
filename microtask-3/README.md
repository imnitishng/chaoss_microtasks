# Microtask 3:
Based on the JSON documents produced by Perceval and its source code, 
try to answer the following questions:

* What is the meaning of the JSON attribute `timestamp`?
    
    The attribute `timestamp` is the datetime format attribute storing the timestamp of when the particular item was fetched.
    
    
* What is the meaning of the JSON attribute `updated_on`?
    
    This attribute stores the UNIX timestamp for when the item was updated originally. This data is taken from already existing fields in data like 'CommitDate' in Git backend and 'update_at' in Mattermost backend.
    
    
* What is the meaning of the JSON attribute `origin`?
    
    This attribute stores the URL of the source from which all the data is being extracted. 
   
  
* What is the meaning of the JSON attribute `category`?
    
    The attribute `category` defines the type of data which is being fetched from the source, this varies for different backends.
    For example the GitHub backend supports categories issue, pull_request and repository, whereas Git backend supports category commits.
    

* How many categories do the GitHub and GitLab backends have?

    Git backend has only one category, namely `commits`.
    GitHub backend has three categories, namely `issues`, `pull_request` and `repository`.
    

* What is the meaning of the JSON attribute 'uuid'?
    
    The `uuid` attribute is a unique id assigned to each item based on the data they have, hence guaranteeing uniqueness. The UUID is SHA1 of the concatenation of the values
    from the list passed as argument to the `uuid()` function. The arguments passed are different for different backends. For instance the Git backend uses `uri` for git repository and `item['commit']` to calculate the unique UUID for every item.
    Another backend mattermost uses `itemp['id']` and combined URL made my joining URL and channel.
    

* What is the meaning of the JSON attribute search_fields?

    The attribute 'search_fields' adds extra fields for search about the item fetched by Perceval. 
    The 'search_fields' for GitLab backend include, `id`, `owner`, `iid`, `project` and `groups`.


* What is stored in the attribute data of each JSON document produced by Perceval?
    
    The attribute ['data'](https://github.com/chaoss/grimoirelab-perceval/blob/75be46b381f30440efeba7497f6756e64d26a0d9/perceval/backend.py#L340)
    stores the actual data which is fetched from the data source. 
    In case, the data to be fetched is issues from Github backend, the issue data will
    be stored in the 'data' attribute. 


