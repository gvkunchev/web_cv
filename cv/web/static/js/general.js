$(document).ready(function(){
    $('.filter-trigger').click(function(){
        var category = $(this).data('category');
        if (category == 'all'){
            $('.timeline-item').show();
        }
        else{
            $('.timeline-item').not("[data-category='" + category + "']").hide();
            $('.timeline-item').filter("[data-category='" + category + "']").show();
        }
        $('#current_category').html($(this).html());
    })
})