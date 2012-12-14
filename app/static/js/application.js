$(function() {
	// All pages
	$('#login_form').submit(function() {
		$('.init-hide').hide();
		
		$.ajax($(this).attr('action'), {
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
	
	if ($.isFunction($.fn.wysihtml5))
		$('#id_description').wysihtml5();
	
	// Equal thumbnail height
	var maxHeight = 30;
	$('.thumbnail').each(function() {
		if ($(this).height() > maxHeight)
			maxHeight = $(this).height();
	});
	$('.thumbnail').css('min-height', maxHeight + 'px');
	
	// Project tasks
	$('#task_add_form').submit(function() {
		$('.init-hide').hide();
		$('.init-no-error').removeClass('error');
		
		$.post($(this).attr('action'), $(this).serialize(), function(data) {
			if (data.success) {
				$('#task_success').text(data.success).show();
				$('.init-clear').val('');
			}
			
			if (data.error)
				$('#task_error').text(data.error).show();
			
			if (data.errors) {
				$.each(data.errors, function(id, message) {
					$('#control_' + id).addClass('error');
					$('#error_' + id).text(message).show();
				});
			}
		});
		
		return false;
	});
})