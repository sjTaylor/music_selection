import React from 'react';
import renderer from 'react-test-renderer';
import NewIndexView from './';
// import data from './IndexView.json';

describe('<NewIndexView />', () => {
    it('Renders an empty IndexView', () => {
        const componentJson = renderer
            .create(<NewIndexView />)
            .toJSON();
        expect(componentJson).toBeTruthy();
    });

    /*
    it('Renders IndexView with data', () => {
        const componentJson = renderer
            .create(<IndexView {...data} />)
            .toJSON();
        expect(componentJson).toMatchSnapshot();
    });
    */
});
