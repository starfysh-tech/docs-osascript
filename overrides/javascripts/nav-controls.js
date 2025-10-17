(function () {
  function ready(fn) {
    if (document.readyState !== "loading") {
      fn();
    } else {
      document.addEventListener("DOMContentLoaded", fn);
    }
  }

  ready(function () {
    var sidebar = document.querySelector('[data-md-component="sidebar"] [data-md-component="primary"] .md-sidebar__scrollwrap');
    if (!sidebar) {
      return;
    }

    var container = document.createElement('div');
    container.className = 'nav-controls';

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'nav-controls__btn';
    button.setAttribute('aria-pressed', 'false');
    button.textContent = 'Expand all';

    container.appendChild(button);
    sidebar.prepend(container);

    var toggles = function () {
      return Array.prototype.slice.call(document.querySelectorAll('[data-md-component="primary"] .md-nav__toggle'));
    };

    var syncNavVisibility = function () {
      toggles().forEach(function (toggle) {
        var sibling = toggle.nextElementSibling;
        while (sibling && sibling.classList && !sibling.classList.contains('md-nav')) {
          sibling = sibling.nextElementSibling;
        }
        if (sibling && sibling.classList && sibling.classList.contains('md-nav')) {
          var expanded = toggle.checked || toggle.indeterminate;
          sibling.hidden = !expanded;
        }
      });
    };

    var updateLabel = function () {
      var toggleList = toggles();
      var allOpen = toggleList.length > 0 && toggleList.every(function (toggle) {
        return toggle.checked || toggle.indeterminate;
      });
      button.textContent = allOpen ? 'Collapse all' : 'Expand all';
      button.setAttribute('aria-pressed', allOpen ? 'true' : 'false');
    };

    button.addEventListener('click', function () {
      var toggleList = toggles();
      if (!toggleList.length) {
        return;
      }
      var shouldExpand = toggleList.some(function (toggle) { return !toggle.checked && !toggle.indeterminate; });
      toggleList.forEach(function (toggle) {
        if (toggle.checked !== shouldExpand || toggle.indeterminate) {
          toggle.indeterminate = false;
          toggle.checked = shouldExpand;
          toggle.dispatchEvent(new Event('change', { bubbles: true }));
        }
      });
      syncNavVisibility();
      updateLabel();
    });

    document.addEventListener('change', function (event) {
      if (event.target && event.target.classList.contains('md-nav__toggle')) {
        syncNavVisibility();
        updateLabel();
      }
    });

    syncNavVisibility();
    updateLabel();
    setTimeout(syncNavVisibility, 60);
  });
})();
