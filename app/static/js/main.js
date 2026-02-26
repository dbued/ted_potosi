// Scripts personalizados
$(function () {
  // Activar tooltips (si se usan)
  $('[data-toggle="tooltip"]').tooltip();

  // Cerrar sidebar automáticamente en móviles al hacer clic en un enlace
  if ($(window).width() < 768) {
    $('.nav-link').on('click', function() {
      $('body').removeClass('sidebar-open');
      $('body').addClass('sidebar-collapse');
    });
  }
});