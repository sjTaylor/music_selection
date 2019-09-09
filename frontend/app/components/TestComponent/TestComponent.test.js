import React from 'react';
import renderer from 'react-test-renderer';
import TestComponent from './';
// import data from './TestComponent.json';

describe('<TestComponent />', () => {
    it('Renders an empty TestComponent', () => {
        const componentJson = renderer
            .create(<TestComponent />)
            .toJSON();
        expect(componentJson).toBeTruthy();
    });

    /*
    it('Renders TestComponent with data', () => {
        const componentJson = renderer
            .create(<TestComponent {...data} />)
            .toJSON();
        expect(componentJson).toMatchSnapshot();
    });
    */
});
