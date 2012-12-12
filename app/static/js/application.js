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
	
	if ($('#id_description')[0])
		$('#id_description').wysihtml5();
	
	// Equal thumbnail height
	var maxHeight = 30;
	$('.thumbnail').each(function() {
		if ($(this).height() > maxHeight)
			maxHeight = $(this).height();
	});
	$('.thumbnail').css('min-height', maxHeight + 'px');
})