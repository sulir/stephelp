$(function() {
	// jQuery plugins
	$('select').selectpicker();
	
	if ($.isFunction($.fn.wysihtml5))
		$('.html-editor').wysihtml5();
	
	// X-editable
	if ($.isFunction($.fn.editable)) {
		$('[data-name][data-url]').editable({
			pk: '0',
			params: {csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
		});
		
		var states = [
  			{value: 'P', text: "planned"},
			{value: 'L', text: "launched"},
			{value: 'F', text: "finished"}
		];
		
		$('[data-name=status]').editable('option', 'source', states).on('save', function(e, params) {
			var self = $(this);
			
			// This should be probably done automatically, but is not.
			$.each(states, function(index, value) {
				if (value.value == params.newValue)
					self.text(value.text);
			});
		})
		
		$('[data-type=select]').on('shown', function() {
			$('select.input-medium').selectpicker();
		})
	}
	
	// Data-assign "nanoframework"
	$('[data-id]').click(function() {
		$('#' + $(this).attr('data-id')).val($(this).attr('data-value'));
	});
	
	// Login form
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
	
	// "Login" link anywhere on a page
	$('.open_login').click(function() {
		$('.dropdown-toggle').dropdown('toggle');
		return false;
	});
	
	// Do not close the login box after clicking on the input
	$('.nav .dropdown input').click(function(event) {
		event.stopPropagation();
	});
	
	// Equal thumbnail height
	var maxHeight = 30;
	$('.thumbnail').each(function() {
		if ($(this).height() > maxHeight)
			maxHeight = $(this).height();
	});
	$('.thumbnail').css('min-height', maxHeight + 'px');
	
	// Project task adding
	$('#task_add_form').submit(function() {
		$('.init-hide').hide();
		$('.init-no-error').removeClass('error');
		
		$.post($(this).attr('action'), $(this).serialize(), function(data) {
			if (data.success) {
				$('#task_list').load($('#task_list').attr('data-url'));
				$('#task_success').text(data.success).show();
				$('input.init-clear').val('');
				$('select.init-clear').prop('selectedIndex', 0).trigger('change');
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