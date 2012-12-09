$(function() {
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
})