// Main Js File

var Molla = [];

( function ($) {
	'use strict';

	var sticky_header_height = 0,
		desktop_width = 992,
		section_ids = [];

	var self = Molla = {
		initialised: false,
		mobile: false,
		init: function() {
			if (!this.initialised) {
				this.initialised = true;
			} else {
				return;
			}

			// Molla functions
			self.fillEmptyDemos(); // For only needed in landing page.
			self.getScrollbarWidth();
			self.headerHeight();
			self.stickyHeaderHeight();
			self.stickyHeader();
			self.dropdownToggle();
			self.mobileMenu();
			self.magnificPopup();
			self.isotopeInit();
			self.countDown();
			self.countTo();
			self.scrollTo();
			self.scrollToTop();
			self.lazyloadImg();
			self.fitVid();
			self.floatElements();
			self.appearAnimate();
			self.windowEvents();
			self.videoControl();
		},
		requestTimeout: function(fn, delay) {
			var handler = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame;
			if ( ! handler ) {
				return setTimeout(fn, delay);
			}
			var start, rt = new Object();

			function loop( timestamp ) {
				if ( ! start ) {
					start = timestamp;
				}
				var progress = timestamp - start;
				progress >= delay ? fn.call() : rt.val = handler( loop );
			};

			rt.val = handler( loop );
			return rt;
		},
		getScrollbarWidth: function() {
			if (self.scrollbarSize === undefined) {
				var scrollDiv = document.createElement("div");
				scrollDiv.style.cssText = 'width: 99px; height: 99px; overflow: scroll; position: absolute; top: -9999px;';
				document.body.appendChild(scrollDiv);
				self.scrollbarSize = scrollDiv.offsetWidth - scrollDiv.clientWidth;
				document.body.removeChild(scrollDiv);
			}
			return self.scrollbarSize;
		},
		calcDesktopWidth: function() {
			desktop_width = 992 - self.getScrollbarWidth();
		},
		headerHeight: function() {
			return $('header:not(.fixed-header)').outerHeight();
		},
		stickyHeaderHeight: function() {
			$('.sticky-wrapper').each(function() {
				var $sticky_header = $(this).find('.sticky-header');
				$sticky_header.addClass('fixed');
				sticky_header_height += $sticky_header.outerHeight();
				$sticky_header.removeClass('fixed');
			})
		},
		stickyHeader: function() {
			// Sticky header 
			var $header = $('.header');
			var height = $header.height(),
				sticky_offset = 0,
				active_toggle = 0;

			// get sticky offset
			if ( $header.data('stickyOffset') ) {
				sticky_offset = parseInt( $header.data('stickyOffset') );
			}

			$(window).on('load scroll resize', function() {
				height = $('.header').height() + sticky_offset;

				if ( $('.sticky-header').length && $(window).width() >= desktop_width ) {
					if ( $(window).scrollTop() > height ) {
						$('.sticky-header').each(function() {
							if ( ! $(this).hasClass('fixed') ) {
								var $this = $(this);
								$this.closest('.sticky-wrapper').height($this.outerHeight() + 'px');
								if (!$this.hasClass('fixed')) {
									active_toggle = $this.find('.dropdown-menu-wrapper.open-toggle').hasClass('show');
								}
								$this.addClass('fixed');
								$('body').hasClass('home') && $this.find('.dropdown-menu-wrapper.open-toggle').removeClass('show');
							}
						})
					}
					else {
						$('body').hasClass('home') && $('.dropdown-menu-wrapper.open-toggle').each(function() {
							var $this = $(this);
							if ( active_toggle ) {
								$this.closest('.sticky-header').hasClass('fixed') && $this.addClass('show');
							}
						});

						$('.sticky-header').removeClass('fixed');
						$('.sticky-header').css('top', '');
					}
					var sticky_height = $('#wpadminbar').height();
					var z_index = $('.sticky-header.fixed').css('z-index');
					var $last_sticky = $('.sticky-header.fixed');
					$('.sticky-header.fixed').each(function() {
						$last_sticky = $(this);
						if ( ! sticky_height ) {
							sticky_height = 0;
						}
						$(this).css('top', sticky_height + 'px');
						sticky_height += $(this).outerHeight();
						$(this).css('z-index', z_index);
						z_index --;
					})
					$last_sticky.parent().siblings('.sticky-wrapper').find('.sticky-header.fixed').css('box-shadow', 'none');
				}
			})
		},
		dropdownToggle: function() {
			$('.dropdown-menu-wrapper.open-toggle>.dropdown-toggle').on('click', function(e) {
				$(this).parent().toggleClass('show').data('closable', true);
				e.preventDefault();
				e.stopPropagation();
			});

			$('body').on('click', function() {
				$('.dropdown-menu-wrapper.open-toggle.show').each(function() {
					var $this = $(this);
					$this.data('closable') && $this.removeClass('show');
				});
			})
		},
		mobileMenu: function() {
			// Mobile Menu Toggle - Show & Hide
			$('.mobile-menu-toggler').on('click', function (e) {
				$('body').toggleClass('mmenu-active');
				$(this).toggleClass('active');
				e.preventDefault();
			});

			$('.mobile-menu-overlay, .mobile-menu-close').on('click', function (e) {
				$('body').removeClass('mmenu-active');
				$('.menu-toggler').removeClass('active');
				e.preventDefault();
			});

			// Mobile Menu toggle children menu
			$('body').on('click', '.mmenu-btn', function (e) {
				var $parent = $(this).closest('li'),
					$targetUl = $parent.find('ul').eq(0);

				if ( !$parent.hasClass('open') ) {
					$targetUl.slideDown(300, function () {
						$parent.addClass('open');
					});
				} else {
					$targetUl.slideUp(300, function () {
						$parent.removeClass('open');
					});
				}

				e.stopPropagation();
				e.preventDefault();
			});
		},
		magnificPopup: function() {
			// Popup - Iframe Video - Map etc.
			if ( $.fn.magnificPopup ) {
				$('.btn-iframe').magnificPopup({
					type: 'iframe',
					removalDelay: 600,
					preloader: false,
					fixedContentPos: false,
					closeBtnInside: false
				});
			}
		},
		layoutInit: function( $container, selector) { // Init Isotope
			if ( ! $.fn.isotope || $container.hasClass('float-grid') ) {
				return;
			}

			if ( undefined == selector ) {
				selector = '.grid-item';
			}

			var isotopeSettings = {
				itemSelector: selector,
				layoutMode: 'masonry',
				getSortData: {
					order: '[data-creative-order] parseInt',
					order_lg: '[data-creative-order-lg] parseInt',
					order_md: '[data-creative-order-md] parseInt',
				},
			};

			if (undefined == $container) {
				$('body').find('[data-toggle="isotope"]').each(function() {
					var $this = $(this);
					var options = $this.data('isotope-options'),
						newIsotopeSettings = $.extend({}, isotopeSettings, options);

					$this.isotope(newIsotopeSettings);
					self.isotopeFilter( $this.siblings('.nav-filter'), $this );
				})
			} else if ( $container.data('toggle') == 'isotope' ) {
				Object.setPrototypeOf($container.get(0), HTMLElement.prototype);
				$container.find(selector).each(function() {
					Object.setPrototypeOf($(this).get(0), HTMLElement.prototype);
				})

				var options = $container.data('isotope-options'),
					newIsotopeSettings = $.extend({}, isotopeSettings, options);

				$container.isotope(newIsotopeSettings);
				self.isotopeFilter( $container.siblings('.nav-filter'), $container );
			}

			self.requestTimeout(function() {
				$(window).trigger('scroll');
			}, 500);

			$(window).on('resize', function(e) {
				if ( undefined == $container ) {
					$('body').find('[data-toggle="isotope"] .grid-item:not(.appear-animate)').css('animation-fill-mode', 'none').css('-webkit-animation-fill-mode', 'none');
					$('body').find('[data-toggle="isotope"] .grid-item.appear-animate.animated').css('animation-fill-mode', 'none').css('-webkit-animation-fill-mode', 'none');
				} else {
					$container.find('.grid-item:not(.appear-animate)').css('animation-fill-mode', 'none').css('-webkit-animation-fill-mode', 'none');
					$container.find('.grid-item.appear-animate.animated').css('animation-fill-mode', 'none').css('-webkit-animation-fill-mode', 'none');
				}
			})
		},
		isotopeFilter: function( $filterNav, $container ) {
			$filterNav.find('a').on('click', function(e) {
				var $this = $(this),
					filter = $this.attr('data-filter');

				// Remove active class
				$filterNav.find('.active').removeClass('active');

				$container.isotope({
					filter: filter,
					transitionDuration: '0.5s'
				});
				$container.css('transition', 'height .5s');
				self.requestTimeout(function() {
					$(window).trigger('scroll');
				}, 500);

				// Add active class
				$this.closest('li').addClass('active');
				e.preventDefault();
			});

			$filterNav.find('li:first-child > a').trigger('click');
			$container.addClass('loaded');
		},
		isotopeInit: function() {
			if ( ! $.fn.isotope )
				return;

			/* Masonry / Grid Layout & Isotope Filter for blog/portfolio etc... */
			$('[data-toggle="isotope"]').each(function() {
				var $this = $(this);
				if ( typeof imagesLoaded === 'function' ) {
					$(this).imagesLoaded(function() {
						self.layoutInit($this); // container - selector
						if ( $('.product-filter').length ) {
							self.isotopeFilter($('.product-filter'), $this);
						}
					})
				} else {
					self.layoutInit($this); // container - selector
					if ( $('.product-filter').length ) {
						self.isotopeFilter($('.product-filter'), $this);
					}
				}
			})
		},
		countDown: function($wrap) {
			if ( $.fn.countdown ) {

				if ( typeof $wrap == 'undefined' ) {
					$wrap = $('body');
				}

				$wrap.find('.deal-countdown').each(function () {
					if (typeof $(this).data('countdown_initialized') != 'undefined' && $(this).data('countdown_initialized')) {
						return;
					}

					var $this = $(this), 
						untilDate = $this.data('until'),
						compact = $this.data('compact'),
						dateFormat = ( !$this.data('format') ) ? 'DHMS' : $this.data('format'),
						newLabels = ( !$this.data('labels-short') ) ? 
										['Years', 'Months', 'Weeks', 'Days', 'Hours', 'Minutes', 'Seconds'] :
										['Years', 'Months', 'Weeks', 'Days', 'Hrs', 'Mins', 'Secs'],
						newLabels1 = ( !$this.data('labels-short') ) ? 
										['Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second'] :
										['Year', 'Month', 'Week', 'Day', 'Hr', 'Min', 'Sec'];

					if ( $(this).hasClass('user_tz') ) {
						$this.countdown({
							until: ( !$this.data('relative') ) ? new Date(untilDate) : untilDate,
							format: dateFormat,
							padZeroes: true,
							compact: compact,
							compactLabels: ['y', 'm', 'w', ' days,'],
							timeSeparator: ' : ',
							labels: newLabels,
							labels1: newLabels1,
							serverSync: new Date( $(this).data('time-now') )
						});
					} else {
						$this.countdown({
							until: ( !$this.data('relative') ) ? new Date(untilDate) : untilDate,
							format: dateFormat,
							padZeroes: true,
							compact: compact,
							compactLabels: ['y', 'm', 'w', ' days,'],
							timeSeparator: ' : ',
							labels: newLabels,
							labels1: newLabels1
						});
					}
					$(this).attr('data-countdown_initialized', true);
				});
			}
		},
		countTo: function($wrap) {
			// Count
			$('.count').each( function() {
				var $countItem = $(this);

				if ( $.fn.countTo && $countItem.attr('data-to') ) {

					// Start counting after appeared
					var defer_appear = (function() {
						var deferred = $.Deferred();
						if ( ! $countItem.closest('.appear-animate').length ) {
							deferred.resolve();
						} else {
							var $appearItem = $countItem.closest('.appear-animate'),
								time = 0,
								options = $appearItem.attr('data-appear-options');

							if (typeof options == 'string') {
								options = JSON.parse(options.replace(/'/g,'"').replace(';',''));
							}

							time += ( undefined == options.delay ? 0 : options.delay );
							time += ( undefined == options.duration ? 1500 : options.duration );

							$appearItem.appear(function() {
								setTimeout(function() {
									deferred.resolve();
								}, time )
							});
						}
						return deferred.promise();
					})();
					$.when(defer_appear).done(function(e) {
						if ($.fn.waypoint) {
							$countItem.waypoint( function () {
								$(this.element).countTo();
							}, {
								offset: '90%',
								triggerOnce: true 
							});
						} else {
							$countItem.countTo();
						}
					});
				}
			})
		},
		scrollTo: function() {
			// Scroll To button
			var $scrollTo = $('.scroll-to');
			// If button scroll elements exists
			if ( $scrollTo.length ) {
				// Scroll to - Animate scroll
				$scrollTo.on('click', function(e) {
					var target = $(this).attr('href');

					if (target.indexOf('#') == 0) {
						var $target = $(target);
					} else {
						var url = window.location.href;
						url = url.substring(url.indexOf('://') + 3);
						if (url.indexOf('#') != -1)
							url = url.substring(0, url.indexOf('#'));
						target = target.substring(target.indexOf('://') + 3);
						target = target.substring(target.indexOf(url) + url.length);

						if (target.indexOf('#') == 0) {
							var $target = $(target);
						}
					}

					if ($target.length) {
						// Add offset for sticky menu
						var scrolloffset = ( $(window).width() >= desktop_width ) ? ($target.offset().top - sticky_header_height) : $target.offset().top;
						$('html, body').animate({
							'scrollTop': scrolloffset
						}, 600);
						e.preventDefault();
					}
				});
			}
		},
		scrollToTop: function() {
			// Scroll Top Button - Show
			var $scrollTop = $('#scroll-top');

			$(window).on('load scroll', function() {
				if ( $(window).scrollTop() >= 400 ) {
					$scrollTop.addClass('show');
				} else {
					$scrollTop.removeClass('show');
				}
			});

			// On click animate to top
			$scrollTop.on('click', function (e) {
				$('html, body').animate({
					'scrollTop': 0
				}, 800);
				e.preventDefault();
			});
		},
		lazyloadImg: function($selector) {
			if ( undefined == $selector ) {
				$selector = $('body');
			}
			if (!$.fn.lazyload) {
				return;
			}

			$selector.find('.molla-lazyload, .molla-lazyload-back').each(function() {
				$(this).lazyload({
					effect: 'fadeIn',
					effect_speed: 400,
					appear: function(elements_left, settings) {

					},
					load: function(elements_left, settings) {
						if ( $(this).hasClass('molla-lazyload') ) {
							$(this).css('padding-top', '').removeClass('molla-lazyload');
						} else {
							$(this).removeClass('molla-lazyload-back');
						}
					}
				})
			})
		},
		fitVid: function() {
			// fit video
			if ( $.fn.fitVids ) {
				$('.fit-video').fitVids();
				$(window).on('resize', function() {
					$('.fit-video').fitVids();
				});
			}
		},
		fillEmptyDemos: function() {
			// Fill Empty Demos

			var filters = $('#sectionDemos .demo-filter a'),
				lackCount = 0,
				filter = '';
			var opt, delay;

			for ( var i = 0; i < filters.length; i++ ) {
				filter = $(filters[i]).attr('data-filter');
				lackCount = $('#sectionDemos .grid-item' + filter).length;
				lackCount = Math.ceil(lackCount / 4) * 4 - lackCount;
				for ( ; lackCount > 0; lackCount-- ) {
					if ( 1 == lackCount % 4 ) {
						delay = 400;
					} else if ( 2 == lackCount % 4 ) {
						delay = 200;
					} else if ( 3 == lackCount % 4 ) {
						delay = 800;
					}
					opt = {
						'name': 'fadeInUpShort',
						'delay': delay
					};

					$('#sectionDemos .grid').append('<div class="grid-item ' + filter.slice(1) + '"><a class="demo-item coming-soon appear-animate" data-appear-options=' + JSON.stringify(opt) + '></a></div>');
				}
			}
		},
		floatElements: function() {
			if ( $.fn.parallax ) {
				$('[data-toggle="floating"]').each( function(e){
					$(this).parallax();
				});
			}
		},
		appearAnimate: function() {
			$('.appear-animate:not(.animated)').each(function(){
				$(this).appear(function() {
					var $this = $(this),
						options = $this.attr('data-appear-options');

					if (typeof options == 'string') {
						options = JSON.parse(options.replace(/'/g,'"').replace(';',''));
					}

					$this.css('animation-duration', ( undefined == options.duration ? 1000 : options.duration ) + 'ms');
					if ( undefined != options.delay ) {
						$this.css('animation-delay', options.delay + 'ms');
					}
					if ( undefined != options.timing ) {
						$this.css('animation-timing-function', options.timing);
					}
					$this.addClass(( undefined == options.name ? 'fadeIn' : options.name ) + ' animated');
				});
			});
		},
		checkScrollSection: function() {
			var cur_pos = $(window).scrollTop(), // Current Scroll Position
				sh = $('.sticky-header.fixed').innerHeight(), // Sticky Header Height
				wh = $(window).height() - sh; // Window Height

			if ( $.isArray(section_ids) ) {
				var idx = -1;

				for (var i = 0; i < section_ids.length; i++) {
					if ( cur_pos + sh + wh / 2 >= $(section_ids[i])[0].offsetTop ) { // if scrollable section is below half of window height
						idx = i;
					} else {
						break;
					}
				}

				if ( idx == -1 ) {
					$('#main-menu > li').removeClass('active');
				} else {
					$('#main-menu > li').eq(idx).addClass('active').siblings().removeClass('active');
				}
			}
		},
		videoControl: function() {
			$('.video-play').on('click', function (e) {
				var $video = $(this).closest('.intro-video');
				if($video.hasClass('playing')) {
					$video.removeClass('playing')
						.addClass('paused')
						.find('video')[0].pause();
				} else {
					$video.removeClass('paused')
						.addClass('playing')
						.find('video')[0].play();
				}
				e.preventDefault();
			});
			$('.intro-video video').on('ended', function() {
				$(this).closest('.intro-video').removeClass('playing');
			});
		},
		windowEvents: function() {
			$(window).on('load resize', function() {
				self.calcDesktopWidth();
			})
			$(window).on('load scroll resize', function(e) {
				self.checkScrollSection();
			})
		}
	};

	// Load Event
	$(window).on('load', function () {
		$('#main-menu .scroll-to').each(function() {
			section_ids.push($(this).attr('href'));
		})

		Molla.init();
		$('body').addClass("loaded");
	});
})(jQuery);
