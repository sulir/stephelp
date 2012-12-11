$(function() {
	// All pages
	$('#login_form').submit(function() {
		$('#login_error').hide();
		
		$.ajax('/login/', {
			type: 'POST',
			data: $(this).serialize(),
			success: function(data) {
				location.reload();
			},
			error: function(xhr) {
				$('#login_error').text(xhr.responseText).show();
			}
		});
		
		return false;
	});
	
	// Create project page
	$('.dropdown input').click(function(event) {
		event.stopPropagation();
	});
	
	$('#open_login').click(function() {
		$('.dropdown-toggle').dropdown('toggle');
		return false;
	});
	
	$('#id_description').wysihtml5();
})