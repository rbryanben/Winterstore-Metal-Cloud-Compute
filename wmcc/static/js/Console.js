let ApplicationData =  {
    "instances" : null,
    "showCreateInstance" : false,
}

const MainApplication = new Vue({
    delimiters : ['[[',']]'],
    el : "#application",
    data : ApplicationData,
    mounted: function(){
        //context 
        var context = this

        //instances
        this.updateInstances()

        // Socket Functions
        const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/server/'
            + 'cloud'
            + '/'
        );

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            context.updateInstances()
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

    },
    methods : {
        //updates the present instances
        updateInstances : function(){
            //context 
            var context = this 

            //get instances
            getInstances(function(data){
                context.instances = JSON.parse(data)  
            })
        },
    }
})