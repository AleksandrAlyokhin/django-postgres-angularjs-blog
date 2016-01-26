describe('Project Admin API:', function() {
  var mytools = require('./../tools.js');

  var listResponse = undefined, updateResponse = undefined, deleteResponse = undefined;

  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        mytools.getJson('/project/list', function(response){
            listResponse = response;
            var record = listResponse.data.records[0];

            mytools.postJson('/project/update/'+record.id, record, function(response){
                updateResponse = response;

                mytools.postJson('/project/delete/'+record.tags[0].id, {}, function(response){
                    deleteResponse = response;

                    done();
                })
            })
        })
    });
  });

  it('get /project/list and check structure', function() {
    expect(typeof listResponse).toEqual('object');
    expect(listResponse.code).toEqual('ok');
    var record = listResponse.data.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof listResponse.data.pageNumber).toEqual('number');
    expect(typeof listResponse.data.countRecordsOnPage).toEqual('number');
    expect(typeof listResponse.data.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/update/:project_id and check structure', function() {
    expect(typeof updateResponse).toEqual('object');
    expect(updateResponse.code).toEqual('ok');
    var record = updateResponse.data;
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/delete/:project_id and check structure', function() {
    expect(typeof deleteResponse).toEqual('object');
    expect(deleteResponse.code).toEqual('ok');
  });


});