/**
 * Displays images of common OpenID providers, allowing the user to
 * select one of them instead of filling in their OpenID URL.
 */

(function() {
    
    /* List of supported providers and their OpenID URLs */
    var providers = {
        'google':   'https://www.google.com/accounts/o8/id',
        'yahoo':    'https://me.yahoo.com',
        'myopenid': 'https://www.myopenid.com'
    };
    
    /* Begin by finding the OpenID input */
    var input = $('#id_openid');
    
    /* Generate a container for the provider buttons */
    var container = $('<div class="openid-container"></div>');
    
    /* Generate each provider and insert it into the container */
    $.each(providers, function(key, value) {
        
        /* Generate the provider */
        var provider = $('<a href="#" class="openid-provider" title="Click to login with this OpenID provider"></a>');
        provider.addClass('openid-provider-' + key);
        
        /* Assign an action when it is clicked */
        provider.click(function() {
            
            /* Fill in and submit the form */
            input.val(value);
            input.closest('form').submit();
            
            return false;
        });
        
        /* Append it to the container */
        container.append(provider);
    });
    
    /* Insert the container before the input */
    container.insertBefore(input);
})();
