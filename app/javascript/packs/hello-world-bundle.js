// Run this example by adding <%= javascript_pack_tag 'hello_world-bundle' %> to the head of your layout file,
// like app/views/layouts/application.html.erb.

import ReactOnRails from 'react-on-rails';

import HelloWorld from '../bundles/HelloWorld/components/HelloWorld';

// This is how react_on_rails can see the HelloWorld in the browser.
ReactOnRails.register({
  HelloWorld,
});
